%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ssd4mosaic
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Web Application for the SSD Module of the MOSAIC Platform

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.4
BuildRequires:    R-CRAN-fitdistrplus >= 1.1.11
BuildRequires:    R-CRAN-golem >= 0.3.5
BuildRequires:    R-CRAN-config >= 0.3.1
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shinybusy 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-shiny >= 1.7.4
Requires:         R-CRAN-fitdistrplus >= 1.1.11
Requires:         R-CRAN-golem >= 0.3.5
Requires:         R-CRAN-config >= 0.3.1
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shinybusy 
Requires:         R-CRAN-shinyjs 
Requires:         R-stats 
Requires:         R-utils 

%description
Web application using 'shiny' for the SSD (Species Sensitivity
Distribution) module of the MOSAIC (MOdeling and StAtistical tools for
ecotoxICology) platform. It estimates the Hazardous Concentration for x%%
of the species (HCx) from toxicity values that can be censored and
provides various plotting options for a better understanding of the
results. See our companion paper Kon Kam King et al. (2014)
<doi:10.48550/arXiv.1311.5772>.

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
