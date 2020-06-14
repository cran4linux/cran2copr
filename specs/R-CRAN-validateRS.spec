%global packname  validateRS
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          One-Sided Multivariate Testing Procedures for Rating Systems

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-triangle 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-triangle 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-data.table 

%description
An implementation of statistical tests for the validation of rating
systems as described in the ECB Working paper ''Advances in multivariate
back-testing for credit risk underestimation'', by F. Coppens, M. Mayer,
L. Millischer, F.  Resch, S. Sauer, K. Schulze (ECB WP series,
forthcoming).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
