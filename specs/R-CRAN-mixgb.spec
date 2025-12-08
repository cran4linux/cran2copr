%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mixgb
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Imputation Through 'XGBoost'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-xgboost >= 3.1.2.1
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-xgboost >= 3.1.2.1
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rfast 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-magrittr 

%description
Multiple imputation using 'XGBoost', subsampling, and predictive mean
matching as described in Deng and Lumley (2023)
<doi:10.1080/10618600.2023.2252501>.  The package supports various types
of variables, offers flexible settings, and enables saving an imputation
model to impute new data. Data processing and memory usage have been
optimised to speed up the imputation process.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
