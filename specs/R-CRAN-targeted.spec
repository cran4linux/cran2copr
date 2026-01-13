%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  targeted
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Targeted Inference

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-lava >= 1.8.2
BuildRequires:    R-CRAN-mets >= 1.3.9
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-lava >= 1.8.2
Requires:         R-CRAN-mets >= 1.3.9
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-R6 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-future.apply 
Requires:         R-methods 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-survival 

%description
Various methods for targeted and semiparametric inference including
augmented inverse probability weighted (AIPW) estimators for missing data
and causal inference (Bang and Robins (2005)
<doi:10.1111/j.1541-0420.2005.00377.x>), variable importance and
conditional average treatment effects (CATE) (van der Laan (2006)
<doi:10.2202/1557-4679.1008>), estimators for risk differences and
relative risks (Richardson et al. (2017)
<doi:10.1080/01621459.2016.1192546>), assumption lean inference for
generalized linear model parameters (Vansteelandt et al. (2022)
<doi:10.1111/rssb.12504>).

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
