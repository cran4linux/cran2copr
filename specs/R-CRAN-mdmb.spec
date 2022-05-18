%global __brp_check_rpaths %{nil}
%global packname  mdmb
%global packver   1.6-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.5
Release:          1%{?dist}%{?buildtag}
Summary:          Model Based Treatment of Missing Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-miceadds >= 3.2.23
BuildRequires:    R-CRAN-CDM 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-sirt 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-miceadds >= 3.2.23
Requires:         R-CRAN-CDM 
Requires:         R-CRAN-coda 
Requires:         R-graphics 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-sirt 
Requires:         R-stats 
Requires:         R-utils 

%description
Contains model-based treatment of missing data for regression models with
missing values in covariates or the dependent variable using maximum
likelihood or Bayesian estimation (Ibrahim et al., 2005;
<doi:10.1198/016214504000001844>; Luedtke, Robitzsch, & West, 2020a,
2020b; <doi:10.1080/00273171.2019.1640104><doi:10.1037/met0000233>). The
regression model can be nonlinear (e.g., interaction effects, quadratic
effects or B-spline functions). Multilevel models with missing data in
predictors are available for Bayesian estimation. Substantive-model
compatible multiple imputation can be also conducted.

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
