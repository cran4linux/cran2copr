%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GeDS
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Geometrically Designed Spline Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mi 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mboost 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-TH.data 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-mi 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mboost 
Requires:         R-parallel 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-TH.data 

%description
Spline Regression, Generalized Additive Models, and Component-wise
Gradient Boosting, utilizing Geometrically Designed (GeD) Splines. GeDS
regression is a non-parametric method inspired by geometric principles,
for fitting spline regression models with variable knots in one or two
independent variables. It efficiently estimates the number of knots and
their positions, as well as the spline order, assuming the response
variable follows a distribution from the exponential family. GeDS models
integrate the broader category of Generalized (Non-)Linear Models,
offering a flexible approach to modeling complex relationships. A
description of the method can be found in Kaishev et al. (2016)
<doi:10.1007/s00180-015-0621-7> and Dimitrova et al. (2023)
<doi:10.1016/j.amc.2022.127493>. Further extending its capabilities,
GeDS's implementation includes Generalized Additive Models (GAM) and
Functional Gradient Boosting (FGB), enabling versatile multivariate
predictor modeling, as discussed in the forthcoming work of Dimitrova et
al. (2025).

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
