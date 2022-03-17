%global __brp_check_rpaths %{nil}
%global packname  dtwclust
%global packver   5.5.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.5.9
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Clustering Along with Optimizations for the Dynamic Time Warping Distance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-RcppParallel >= 4.4.0
BuildRequires:    R-CRAN-proxy >= 0.4.16
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-flexclust 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-RcppParallel >= 4.4.0
Requires:         R-CRAN-proxy >= 0.4.16
Requires:         R-methods 
Requires:         R-CRAN-dtw 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-flexclust 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 

%description
Time series clustering along with optimized techniques related to the
Dynamic Time Warping distance and its corresponding lower bounds.
Implementations of partitional, hierarchical, fuzzy, k-Shape and TADPole
clustering are available. Functionality can be easily extended with custom
distance measures and centroid definitions. Implementations of DTW
barycenter averaging, a distance based on global alignment kernels, and
the soft-DTW distance and centroid routines are also provided. All
included distance functions have custom loops optimized for the
calculation of cross-distance matrices, including parallelization support.
Several cluster validity indices are included.

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
