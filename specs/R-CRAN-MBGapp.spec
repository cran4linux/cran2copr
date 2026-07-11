%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MBGapp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive 'shiny' Application for Model-Based Geostatistics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-geoR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-leafem 
BuildRequires:    R-CRAN-tidyterra 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-RiskMap 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-geoR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-leafem 
Requires:         R-CRAN-tidyterra 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-RiskMap 
Requires:         R-CRAN-terra 
Requires:         R-grDevices 
Requires:         R-CRAN-shinyjs 
Requires:         R-splines 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-rmarkdown 

%description
Provides an interactive 'shiny' application for teaching and applied
analysis of geostatistical data. Users can explore spatial data, assess
spatial correlation through the empirical variogram, fit model-based
geostatistical models for continuous, prevalence and count outcomes,
produce spatial predictions, and download reports. The methodology follows
the model-based geostatistics framework of Diggle and Giorgi (2019,
ISBN:9781138732353).

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
