%global __brp_check_rpaths %{nil}
%global packname  soilassessment
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Assessment Models for Agriculture Soil Conditions and Crop Suitability

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-Cubist 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-FuzzyAHP 
BuildRequires:    R-CRAN-googledrive 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-quantregForest 
BuildRequires:    R-CRAN-qrnn 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-soiltexture 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-Cubist 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-FuzzyAHP 
Requires:         R-CRAN-googledrive 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-kernlab 
Requires:         R-methods 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-quantregForest 
Requires:         R-CRAN-qrnn 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-png 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-soiltexture 
Requires:         R-CRAN-sp 
Requires:         R-stats 

%description
Soil assessment builds information for improved decision in soil
management. It analyzes soil conditions with regard to agriculture crop
suitability requirements [such as those given by FAO
<https://www.fao.org/land-water/databases-and-software/crop-information/en/>]
soil fertility classes, soil erosion models and soil salinity
classification. Suitability requirements are for crops grouped into cereal
crops, nuts, legumes, fruits, vegetables, industrial crops, and root
crops.

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
