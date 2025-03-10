%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rTwig
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Realistic Quantitative Structure Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-R.matlab 
BuildRequires:    R-CRAN-rmatio 
BuildRequires:    R-CRAN-tidytable 
BuildRequires:    R-CRAN-cobs 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-colourvalues 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppSimdJson 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-R.matlab 
Requires:         R-CRAN-rmatio 
Requires:         R-CRAN-tidytable 
Requires:         R-CRAN-cobs 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-colourvalues 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppSimdJson 
Requires:         R-CRAN-geometry 

%description
Real Twig is a method to correct branch overestimation in quantitative
structure models. Overestimated cylinders are correctly tapered using
measured twig diameters of corresponding tree species. Supported
quantitative structure modeling software includes 'TreeQSM',
'SimpleForest', 'Treegraph', and 'aRchi'. Also included is a novel
database of twig diameters and tools for fractal analysis of point clouds.

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
