%global packname  NNMIS
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Nearest Neighbor Based Multiple Imputation for Survival Datawith Missing Covariates

License:          LGPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-survival 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-survival 

%description
Imputation for both missing covariates and censored observations
(optional) for survival data with missing covariates by the nearest
neighbor based multiple imputation algorithm as described in Hsu et al.
(2006) <doi:10.1002/sim.2452>, and Hsu and Yu (2018) <doi:
10.1177/0962280218772592>. Note that the current version can only impute
for a situation with one missing covariate.

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
