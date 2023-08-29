%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GWRLASSO
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Hybrid Model for Spatial Prediction Through Local Regression

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-qpdf 
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-qpdf 
Requires:         R-CRAN-numbers 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-Matrix 

%description
It implements a hybrid spatial model for improved spatial prediction by
combining the variable selection capability of LASSO (Least Absolute
Shrinkage and Selection Operator) with the Geographically Weighted
Regression (GWR) model that captures the spatially varying relationship
efficiently. For method details see, Wheeler,
D.C.(2009).<DOI:10.1068/a40256>. The developed hybrid model efficiently
selects the relevant variables by using LASSO as the first step; these
selected variables are then incorporated into the GWR framework, allowing
the estimation of spatially varying regression coefficients at unknown
locations and finally predicting the values of the response variable at
unknown test locations while taking into account the spatial heterogeneity
of the data. Integrating the LASSO and GWR models enhances prediction
accuracy by considering spatial heterogeneity and capturing the local
relationships between the predictors and the response variable. The
developed hybrid spatial model can be useful for spatial modeling,
especially in scenarios involving complex spatial patterns and large
datasets with multiple predictor variables.

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
