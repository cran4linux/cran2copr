%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spatialAtomizeR
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Analysis with Misaligned Data Using Atom-Based Regression Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nimble 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-BiasedUrn 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
Requires:         R-CRAN-nimble 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-BiasedUrn 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-methods 

%description
Implements atom-based regression models (ABRM) for analyzing spatially
misaligned data. Provides functions for simulating misaligned spatial
data, preparing NIMBLE model inputs, running MCMC diagnostics, and
comparing different spatial analysis methods including dasymetric mapping.
All main functions return S3 objects with print(), summary(), and plot()
methods for intuitive result exploration. Methods are described in Nethery
et al. (2023) <doi:10.1101/2023.01.10.23284410>. Further methodological
details and software implementation are described in Qian et al. (in
review).

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
