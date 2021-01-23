%global packname  sdmApp
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          A User-Friendly Application for Species Distribution Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest >= 4.6.10
BuildRequires:    R-CRAN-biomod2 >= 3.4.6
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-raster >= 2.6.7
BuildRequires:    R-CRAN-haven >= 2.3.1
BuildRequires:    R-CRAN-blockCV >= 2.1.1
BuildRequires:    R-CRAN-readxl >= 1.3.1
BuildRequires:    R-CRAN-tidyverse >= 1.3.0
BuildRequires:    R-CRAN-sp >= 1.2.0
BuildRequires:    R-CRAN-CENFA >= 1.1.0
BuildRequires:    R-CRAN-dismo >= 1.0.12
BuildRequires:    R-CRAN-kernlab >= 0.9.29
BuildRequires:    R-CRAN-rJava >= 0.9.13
BuildRequires:    R-CRAN-shinyFiles >= 0.7.0
BuildRequires:    R-CRAN-shinyBS >= 0.61
BuildRequires:    R-CRAN-ggpubr >= 0.4.0
BuildRequires:    R-CRAN-rgeos >= 0.3.8
BuildRequires:    R-CRAN-rhandsontable >= 0.3.7
BuildRequires:    R-CRAN-SSDM >= 0.2.8
BuildRequires:    R-CRAN-shiny >= 0.12.2
BuildRequires:    R-CRAN-ggcorrplot >= 0.1.3
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-randomForest >= 4.6.10
Requires:         R-CRAN-biomod2 >= 3.4.6
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-raster >= 2.6.7
Requires:         R-CRAN-haven >= 2.3.1
Requires:         R-CRAN-blockCV >= 2.1.1
Requires:         R-CRAN-readxl >= 1.3.1
Requires:         R-CRAN-tidyverse >= 1.3.0
Requires:         R-CRAN-sp >= 1.2.0
Requires:         R-CRAN-CENFA >= 1.1.0
Requires:         R-CRAN-dismo >= 1.0.12
Requires:         R-CRAN-kernlab >= 0.9.29
Requires:         R-CRAN-rJava >= 0.9.13
Requires:         R-CRAN-shinyFiles >= 0.7.0
Requires:         R-CRAN-shinyBS >= 0.61
Requires:         R-CRAN-ggpubr >= 0.4.0
Requires:         R-CRAN-rgeos >= 0.3.8
Requires:         R-CRAN-rhandsontable >= 0.3.7
Requires:         R-CRAN-SSDM >= 0.2.8
Requires:         R-CRAN-shiny >= 0.12.2
Requires:         R-CRAN-ggcorrplot >= 0.1.3
Requires:         R-CRAN-DT 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-data.table 

%description
A 'shiny' application that allows non-expert 'R' users to easily model
species distribution. It offers a reproducible work flow for species
distribution modeling into a single and user friendly environment.
'sdmApp' takes 'raster' data (in format supported by the 'raster package')
and species occurrence data (several format supported) as input argument.
It provides an interactive graphical user interface (GUI).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
