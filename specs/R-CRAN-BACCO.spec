%global packname  BACCO
%global packver   2.0-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.9
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Analysis of Computer Code Output (BACCO)

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-approximator >= 1.2.6
BuildRequires:    R-CRAN-calibrator >= 1.2.5
BuildRequires:    R-CRAN-emulator >= 1.2.13
Requires:         R-CRAN-approximator >= 1.2.6
Requires:         R-CRAN-calibrator >= 1.2.5
Requires:         R-CRAN-emulator >= 1.2.13

%description
The BACCO bundle of packages is replaced by the BACCO package, which
provides a vignette that illustrates the constituent packages (emulator,
approximator, calibrator) in use.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
