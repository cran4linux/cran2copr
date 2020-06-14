%global packname  TInPosition
%global packver   0.13.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.6.1
Release:          2%{?dist}
Summary:          Inference Tests for TExPosition

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ExPosition >= 2.8.19
BuildRequires:    R-CRAN-TExPosition >= 2.6.10
BuildRequires:    R-CRAN-prettyGraphs >= 2.1.4
BuildRequires:    R-CRAN-InPosition >= 0.12.7
Requires:         R-CRAN-ExPosition >= 2.8.19
Requires:         R-CRAN-TExPosition >= 2.6.10
Requires:         R-CRAN-prettyGraphs >= 2.1.4
Requires:         R-CRAN-InPosition >= 0.12.7

%description
Non-parametric resampling-based inference tests for TExPosition.

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
%{rlibdir}/%{packname}/INDEX
