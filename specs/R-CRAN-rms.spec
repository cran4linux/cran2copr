%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rms
%global packver   8.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Modeling Strategies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildRequires:    R-CRAN-Hmisc >= 5.2.4
BuildRequires:    R-CRAN-nlme >= 3.1.123
BuildRequires:    R-CRAN-htmlTable >= 1.11.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-polspline 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-Hmisc >= 5.2.4
Requires:         R-CRAN-nlme >= 3.1.123
Requires:         R-CRAN-htmlTable >= 1.11.0
Requires:         R-methods 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-SparseM 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-polspline 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-knitr 
Requires:         R-grDevices 
Requires:         R-CRAN-scales 

%description
Regression modeling, testing, estimation, validation, graphics,
prediction, and typesetting by storing enhanced model design attributes in
the fit.  'rms' is a collection of functions that assist with and
streamline modeling.  It also contains functions for binary and ordinal
logistic regression models, ordinal models for continuous Y with a variety
of distribution families, and the Buckley-James multiple regression model
for right-censored responses, and implements penalized maximum likelihood
estimation for logistic and ordinary linear models.  'rms' works with
almost any regression model, but it was especially written to work with
binary or ordinal regression models, Cox regression, accelerated failure
time models, ordinary linear models, the Buckley-James model, generalized
least squares for serially or spatially correlated observations,
generalized linear models, and quantile regression.

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
