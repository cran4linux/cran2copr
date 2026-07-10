%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lctools
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Local and Geographically Weighted Spatial Statistics Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
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
Provides researchers and educators with easy-to-learn, user friendly tools
for calculating key spatial statistics and for applying simple as well as
advanced methods of spatial analysis on real data. These include: Local
Pearson and Geographically Weighted Pearson Correlation Coefficients;
Spatial Inequality Measures (Gini coefficient, Spatial Gini, Location
Quotient (LQ) and Focal Location Quotient); Spatial Autocorrelation
indices (Global and Local Moran's I); several Geographically Weighted
Regression techniques, including the Geographically Weighted Zero-Inflated
Poisson Regression; tools for computing variables used in Spatial
Interaction Models; and other spatial analysis tools (other geographically
weighted statistics). The local correlation tools were originally
developed to test for local multicollinearity among the explanatory
variables of local regression models and can also be used to examine the
local association between pairs of variables. The package also contains
functions for measuring the significance of each statistic calculated,
mainly based on Monte Carlo simulations, and comes with two example
datasets, one of which is a spatial data frame referring to the
municipalities of Greece. Methods are described in Kalogirou (2012)
<doi:10.1007/s10037-011-0061-y>, Kalogirou (2016)
<doi:10.1111/gean.12092>, and Rey and Smith (2013)
<doi:10.1007/s12076-012-0086-z>.

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
