%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FuelDeep3D
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          3D Fuel Segmentation Using Terrestrial Laser Scanning and Deep Learning

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-rlang 

%description
Provides tools for preprocessing, feature extraction, and segmentation of
three-dimensional forest point clouds derived from terrestrial laser
scanning. Functions support creating height-above-ground (HAG) metrics,
tiling, and sampling point clouds, generating training datasets, applying
trained models to new point clouds, and producing per-point fuel classes
such as stems, branches, foliage, and surface fuels. These tools support
workflows for forest structure analysis, wildfire behavior modeling, and
fuel complexity assessment. Deep learning segmentation relies on the
PointNeXt architecture described by Qian et al. (2022)
<doi:10.48550/arXiv.2206.04670>, while ground classification utilizes the
Cloth Simulation Filter algorithm by Zhang et al. (2016)
<doi:10.3390/rs8060501>.

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
