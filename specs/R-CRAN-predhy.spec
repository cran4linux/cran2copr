%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  predhy
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Genomic Prediction of Hybrid Performance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BGLR 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-lightgbm 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
Requires:         R-CRAN-BGLR 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-lightgbm 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 

%description
Performs genomic prediction of hybrid performance using eight statistical
methods including GBLUP, BayesB, RKHS, PLS, LASSO, EN, LightGBM and
XGBoost along with additive and additive-dominance models. Users are able
to incorporate parental phenotypic information in all methods based on
their specific needs. (Xu S et al(2017) <doi:10.1534/g3.116.038059>; Xu Y
et al (2021) <doi: 10.1111/pbi.13458>).

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
