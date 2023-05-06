%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geomod
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Computer Program for Geotechnical Investigations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-rasterVis 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-Cubist 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-qrnn 
BuildRequires:    R-CRAN-quantregForest 
BuildRequires:    R-CRAN-nnet 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-rasterVis 
Requires:         R-stats 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-Cubist 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-qrnn 
Requires:         R-CRAN-quantregForest 
Requires:         R-CRAN-nnet 

%description
The 'geomod' does spatial prediction of the Geotechnical soil properties.
It predicts the spatial distribution of Geotechnical properties of soil
e.g. shear strength, permeability, plasticity index, Standard Penetration
Test (SPT) counts, etc. The output of the prediction takes the form of a
map or a series of maps. It uses the interpolation technique where a
single or statistically “best” estimate of spatial occurrence soil
property is determined. The interpolation is based on both the sampled
data and a variogram model for the spatial correlation of the sampled
data. The single estimate is produced by a Kriging technique.

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
