%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  btb
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Beyond the Border - Kernel Density Estimation for Urban Geography

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-BH >= 1.60.0.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mapsf 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mapsf 
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-magrittr 

%description
The kernelSmoothing() function allows you to square and smooth geolocated
data. It calculates a classical kernel smoothing (conservative) or a
geographically weighted median. There are four major call modes of the
function. The first call mode is kernelSmoothing(obs, epsg, cellsize,
bandwidth) for a classical kernel smoothing and automatic grid. The second
call mode is kernelSmoothing(obs, epsg, cellsize, bandwidth, quantiles)
for a geographically weighted median and automatic grid. The third call
mode is kernelSmoothing(obs, epsg, cellsize, bandwidth, centroids) for a
classical kernel smoothing and user grid. The fourth call mode is
kernelSmoothing(obs, epsg, cellsize, bandwidth, quantiles, centroids) for
a geographically weighted median and user grid. Geographically weighted
summary statistics : a framework for localised exploratory data analysis,
C.Brunsdon & al., in Computers, Environment and Urban Systems C.Brunsdon &
al. (2002) <doi:10.1016/S0198-9715(01)00009-6>, Statistical Analysis of
Spatial and Spatio-Temporal Point Patterns, Third Edition, Diggle, pp.
83-86, (2003) <doi:10.1080/13658816.2014.937718>.

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
