%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rasch
%global packver   1.12.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.12.1
Release:          1%{?dist}%{?buildtag}
Summary:          Models and Diagnostics for Rasch Measurement Theory

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 

%description
Fits models for Rasch Measurement Theory, whose defining measurement
properties include sufficiency and invariance. Available models include
the dichotomous Rasch, partial credit, rating scale, many-facet, extended
frame of reference and explanatory models. Explanatory modelling supports
predictors at the item and threshold levels. Comparative judgement models
are available for dichotomous and ordered pairwise responses, with support
for extended frames of reference and explanatory predictors. Functions
support estimation and examination of model fit, targeting, reliability,
dimensionality, local dependence, differential item functioning, equating
and simulation. A graphical interface for fitting models and examining
results is provided through an interactive 'shiny' application.

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
