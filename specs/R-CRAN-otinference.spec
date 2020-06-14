%global packname  otinference
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Inference for Optimal Transport

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.45
BuildRequires:    R-CRAN-sm >= 2.2.5.4
BuildRequires:    R-CRAN-transport >= 0.8.1
BuildRequires:    R-CRAN-Rglpk >= 0.6.2
Requires:         R-MASS >= 7.3.45
Requires:         R-CRAN-sm >= 2.2.5.4
Requires:         R-CRAN-transport >= 0.8.1
Requires:         R-CRAN-Rglpk >= 0.6.2

%description
Sample from the limiting distributions of empirical Wasserstein distances
under the null hypothesis and under the alternative. Perform a two-sample
test on multivariate data using these limiting distributions and binning.

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
%{rlibdir}/%{packname}/INDEX
