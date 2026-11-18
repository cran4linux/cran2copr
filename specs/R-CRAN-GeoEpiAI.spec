%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GeoEpiAI
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          GeoAI and Digital Epidemiology Tools for Disease Surveillance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-xgboost 

%description
Provides tools for digital epidemiology and geospatial artificial
intelligence, including surveillance-data cleaning, spatial epidemiology,
spatial autocorrelation and hotspot detection, environmental data
integration, machine-learning-based disease-risk prediction, dynamic risk
mapping, early-warning detection, and automated epidemiological reporting.
The methods include spatial autocorrelation (Moran, 1950)
<doi:10.1093/biomet/37.1-2.17>, local spatial association analysis (Getis
and Ord, 1992) <doi:10.1111/j.1538-4632.1992.tb00261.x>, Random Forest
(Breiman, 2001) <doi:10.1023/A:1010933404324>, XGBoost (Chen and Guestrin,
2016) <doi:10.1145/2939672.2939785>, and spatial data handling (Pebesma,
2018) <doi:10.32614/RJ-2018-009>. The package supports applications in
disease surveillance, epidemiological risk assessment, and environmental
health.

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
