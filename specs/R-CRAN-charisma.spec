%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  charisma
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reproducible Color Characterization of Digital Images for Biological Studies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-recolorize 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-parallel 
Requires:         R-CRAN-recolorize 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-png 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Provides a standardized and reproducible framework for characterizing and
classifying discrete color classes from digital images of biological
organisms. The package automatically determines the presence or absence of
10 human-visible color categories (black, blue, brown, green, grey,
orange, purple, red, white, yellow) using a biologically-inspired Color
Look-Up Table (CLUT) that partitions HSV color space. Supports both fully
automated and semi-automated (interactive) workflows with complete
provenance tracking for reproducibility. Pre-processes images using the
'recolorize' package (Weller et al. 2024 <doi:10.1111/ele.14378>) for
spatial-color binning, and integrates with 'pavo' (Maia et al. 2019
<doi:10.1111/2041-210X.13174>) for color pattern geometry statistics.
Designed for high-throughput analysis and seamless integration with
downstream evolutionary analyses.

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
