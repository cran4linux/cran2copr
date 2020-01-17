%global packname  lori
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}
Summary:          Imputation of Count Data using Side Information

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rARPACK 
BuildRequires:    R-CRAN-svd 
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rARPACK 
Requires:         R-CRAN-svd 

%description
Analysis, imputation, and multiple imputation of count data using
covariates. LORI uses a log-linear model where main row and column effects
are decomposed as regression terms on known covariates. A residual
low-rank interaction term is also fitted. LORI returns estimates of
covariate effects and interactions, as well as an imputed count table. The
package also contains a multiple imputation procedure.

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
