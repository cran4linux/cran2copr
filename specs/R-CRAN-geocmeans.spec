%global __brp_check_rpaths %{nil}
%global packname  geocmeans
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Implementing Methods for Spatial Fuzzy Unsupervised Classification

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-plotly >= 4.9.3
BuildRequires:    R-stats >= 3.5
BuildRequires:    R-grDevices >= 3.5
BuildRequires:    R-methods >= 3.5
BuildRequires:    R-CRAN-raster >= 3.4.10
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-fclust >= 2.1.1
BuildRequires:    R-CRAN-Rdpack >= 2.1.1
BuildRequires:    R-CRAN-leaflet >= 2.0.4.1
BuildRequires:    R-CRAN-reldist >= 1.6.6
BuildRequires:    R-CRAN-shiny >= 1.6.0
BuildRequires:    R-CRAN-rgdal >= 1.5.23
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-sp >= 1.4.4
BuildRequires:    R-CRAN-future.apply >= 1.4.0
BuildRequires:    R-CRAN-spdep >= 1.1.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.6
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-fmsb >= 0.7.0
BuildRequires:    R-CRAN-matrixStats >= 0.58.0
BuildRequires:    R-CRAN-rgeos >= 0.5.5
BuildRequires:    R-CRAN-progressr >= 0.4.0
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-plotly >= 4.9.3
Requires:         R-stats >= 3.5
Requires:         R-grDevices >= 3.5
Requires:         R-methods >= 3.5
Requires:         R-CRAN-raster >= 3.4.10
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-fclust >= 2.1.1
Requires:         R-CRAN-Rdpack >= 2.1.1
Requires:         R-CRAN-leaflet >= 2.0.4.1
Requires:         R-CRAN-reldist >= 1.6.6
Requires:         R-CRAN-shiny >= 1.6.0
Requires:         R-CRAN-rgdal >= 1.5.23
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-sp >= 1.4.4
Requires:         R-CRAN-future.apply >= 1.4.0
Requires:         R-CRAN-spdep >= 1.1.2
Requires:         R-CRAN-Rcpp >= 1.0.6
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-fmsb >= 0.7.0
Requires:         R-CRAN-matrixStats >= 0.58.0
Requires:         R-CRAN-rgeos >= 0.5.5
Requires:         R-CRAN-progressr >= 0.4.0

%description
Provides functions to apply spatial fuzzy unsupervised classification,
visualize and interpret results. This method is well suited when the user
wants to analyze data with a fuzzy clustering algorithm and to account for
the spatial dimension of the dataset. In addition, indexes for estimating
the spatial consistency and classification quality are proposed. The
methods were originally proposed in the field of brain imagery (seed Cai
and al. 2007 <doi:10.1016/j.patcog.2006.07.011> and Zaho and al. 2013
<doi:10.1016/j.dsp.2012.09.016>) and recently applied in geography (see
Gelb and Apparicio <doi:10.4000/cybergeo.36414>).

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
