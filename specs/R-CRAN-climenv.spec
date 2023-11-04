%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  climenv
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download, Extract and Visualise Climate and Elevation Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-elevatr >= 0.99
BuildRequires:    R-CRAN-climaemet 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-exactextractr 
BuildRequires:    R-CRAN-geodata 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-Ternary 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-elevatr >= 0.99
Requires:         R-CRAN-climaemet 
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-exactextractr 
Requires:         R-CRAN-geodata 
Requires:         R-CRAN-glue 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-Ternary 
Requires:         R-CRAN-terra 

%description
Grants access to three widely recognised modelled data sets, namely Global
Climate Data (WorldClim 2), Climatologies at high resolution for the
earth's land surface areas (CHELSA), and National Aeronautics and Space
Administration's (NASA) Shuttle Radar Topography Mission (SRTM). It
handles both multi and single geospatial polygon and point data, extracts
outputs that can serve as covariates in various ecological studies.
Provides two common graphic options – the Walter-Lieth (1960)
<https://donum.uliege.be/bitstream/2268.1/7079/1/Walter-Lieth_Klimadiagramm-Weltatlas.pdf>
climate diagram and the Holdridge (1967)
<https://reddcr.go.cr/sites/default/files/centro-de-documentacion/holdridge_1966_-_life_zone_ecology.pdf>
life zone classification scheme. Provides one new graphic scheme of our
own design which incorporates aspects of both Walter-Leigh and Holdridge.
Provides user-friendly access and extraction of globally recognisable data
sets to enhance their usability across a broad spectrum of applications.

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
