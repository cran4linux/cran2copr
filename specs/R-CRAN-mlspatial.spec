%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlspatial
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning and Mapping for Spatial Epidemiology

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-tmap 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-tmap 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-ggpubr 
Requires:         R-stats 
Requires:         R-methods 

%description
Provides tools for the integration, visualisation, and modelling of
spatial epidemiological data using the method described in Azeez, A., &
Noel, C. (2025). 'Predictive Modelling and Spatial Distribution of
Pancreatic Cancer in Africa Using Machine Learning-Based Spatial Model'
<doi:10.5281/zenodo.16529986> and <doi:10.5281/zenodo.16529016>. It
facilitates the analysis of geographic health data by combining modern
spatial mapping tools with advanced machine learning (ML) algorithms.
'mlspatial' enables users to import and pre-process shapefile and
associated demographic or disease incidence data, generate richly
annotated thematic maps, and apply predictive models, including Random
Forest, 'XGBoost', and Support Vector Regression, to identify spatial
patterns and risk factors. It is suited for spatial epidemiologists,
public health researchers, and GIS analysts aiming to uncover hidden
geographic patterns in health-related outcomes and inform evidence-based
interventions.

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
