%global __brp_check_rpaths %{nil}
%global packname  EcotoneFinder
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Characterising and Locating Ecotones and Communities

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-philentropy 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rmisc 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-vegclust 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-philentropy 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rmisc 
Requires:         R-stats 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-vegclust 
Requires:         R-CRAN-withr 

%description
Analytical methods to locate and characterise ecotones, ecosystems and
environmental patchiness along ecological gradients. Methods are
implemented for isolated sampling or for space/time series. It includes
Detrended Correspondence Analysis (Hill & Gauch (1980)
<doi:10.1007/BF00048870>), fuzzy clustering (De Cáceres et al. (2010)
<doi:10.1080/01621459.1963.10500845>), biodiversity indices (Jost (2006)
<doi:10.1111/j.2006.0030-1299.14714.x>), and network analyses (Epskamp et
al. (2012) <doi:10.18637/jss.v048.i04>) - as well as tools to explore the
number of clusters in the data. Functions to produce synthetic ecological
datasets are also provided.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
