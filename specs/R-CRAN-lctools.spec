%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lctools
%global packver   0.2-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.10
Release:          1%{?dist}%{?buildtag}
Summary:          Local Correlation, Spatial Inequalities, Geographically Weighted Regression and Other Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-weights 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-weights 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-MASS 

%description
Provides researchers and educators with easy-to-learn user friendly tools
for calculating key spatial statistics and to apply simple as well as
advanced methods of spatial analysis in real data. These include: Local
Pearson and Geographically Weighted Pearson Correlation Coefficients,
Spatial Inequality Measures (Gini, Spatial Gini, LQ, Focal LQ), Spatial
Autocorrelation (Global and Local Moran's I), several Geographically
Weighted Regression techniques and other Spatial Analysis tools (other
geographically weighted statistics). This package also contains functions
for measuring the significance of each statistic calculated, mainly based
on Monte Carlo simulations.

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
