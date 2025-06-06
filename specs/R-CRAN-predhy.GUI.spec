%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  predhy.GUI
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Genomic Prediction of Hybrid Performance with Graphical User Interface

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-predhy >= 2.1.2
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-BGLR 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-lightgbm 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-predhy >= 2.1.2
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-BGLR 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-lightgbm 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-htmltools 

%description
Performs genomic prediction of hybrid performance using eight GS methods
including GBLUP, BayesB, RKHS, PLS, LASSO, Elastic net, XGBoost and
LightGBM. GBLUP: genomic best liner unbiased prediction, RKHS: reproducing
kernel Hilbert space, PLS: partial least squares regression, LASSO: least
absolute shrinkage and selection operator, XGBoost: extreme gradient
boosting, LightGBM: light gradient boosting machine. It also provides fast
cross-validation and mating design scheme for training population (Xu S et
al (2016) <doi:10.1111/tpj.13242>; Xu S (2017)
<doi:10.1534/g3.116.038059>).

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
