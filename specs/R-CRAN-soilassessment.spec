%global __brp_check_rpaths %{nil}
%global packname  soilassessment
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Assessment Models for Agriculture Soil Conditions and CropSuitability

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
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-methods 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-quantregForest 
BuildRequires:    R-CRAN-qrnn 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-soiltexture 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-Cubist 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-FuzzyAHP 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-maptools 
Requires:         R-methods 
Requires:         R-nnet 
Requires:         R-CRAN-quantregForest 
Requires:         R-CRAN-qrnn 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-rpart 
Requires:         R-CRAN-soiltexture 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-utils 

%description
Soil assessment builds information for improved decision in soil
management. It analyzes soil conditions with regard to agriculture crop
suitability requirements [such as those given by FAO
<http://www.fao.org/land-water/databases-and-software/crop-information/en/>]
soil fertility classes, soil erosion models and soil salinity
classification. Suitability requirements are for crops grouped into cereal
crops, nuts, legumes, fruits, vegetables, industrial crops, and root
crops.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
