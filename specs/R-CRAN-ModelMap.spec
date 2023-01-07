%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ModelMap
%global packver   3.4.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Modeling and Map Production using Random Forest and Related Stochastic Models

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-HandTill2001 
BuildRequires:    R-CRAN-PresenceAbsence 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-HandTill2001 
Requires:         R-CRAN-PresenceAbsence 

%description
Creates sophisticated models of training data and validates the models
with an independent test set, cross validation, or Out Of Bag (OOB)
predictions on the training data. Create graphs and tables of the model
validation results. Applies these models to GIS .img files of predictors
to create detailed prediction surfaces. Handles large predictor files for
map making, by reading in the .img files in chunks, and output to the .txt
file the prediction for each data chunk, before reading the next chunk of
data.

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
