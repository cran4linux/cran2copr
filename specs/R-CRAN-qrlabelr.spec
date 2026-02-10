%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qrlabelr
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Machine- And Human-Readable Plot Labels for Experiments

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 3.6.23
BuildRequires:    R-CRAN-ggplot2 >= 3.4.2
BuildRequires:    R-CRAN-shinyjs >= 2.1.0
BuildRequires:    R-CRAN-readxl >= 1.4.1
BuildRequires:    R-CRAN-desplot >= 1.10
BuildRequires:    R-CRAN-dplyr >= 1.0.10
BuildRequires:    R-CRAN-purrr >= 1.0.1
BuildRequires:    R-CRAN-shinycssloaders >= 1.0.0
BuildRequires:    R-CRAN-QBMS >= 0.9.1
BuildRequires:    R-CRAN-shinyWidgets >= 0.7.6
BuildRequires:    R-CRAN-shinyBS >= 0.61.1
BuildRequires:    R-CRAN-reactable >= 0.4.3
BuildRequires:    R-CRAN-bslib >= 0.4.2
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-CRAN-argonDash >= 0.2.0
BuildRequires:    R-CRAN-argonR >= 0.2.0
BuildRequires:    R-CRAN-qrencoder >= 0.1.0
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-raster >= 3.6.23
Requires:         R-CRAN-ggplot2 >= 3.4.2
Requires:         R-CRAN-shinyjs >= 2.1.0
Requires:         R-CRAN-readxl >= 1.4.1
Requires:         R-CRAN-desplot >= 1.10
Requires:         R-CRAN-dplyr >= 1.0.10
Requires:         R-CRAN-purrr >= 1.0.1
Requires:         R-CRAN-shinycssloaders >= 1.0.0
Requires:         R-CRAN-QBMS >= 0.9.1
Requires:         R-CRAN-shinyWidgets >= 0.7.6
Requires:         R-CRAN-shinyBS >= 0.61.1
Requires:         R-CRAN-reactable >= 0.4.3
Requires:         R-CRAN-bslib >= 0.4.2
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-argonDash >= 0.2.0
Requires:         R-CRAN-argonR >= 0.2.0
Requires:         R-CRAN-qrencoder >= 0.1.0
Requires:         R-grid 
Requires:         R-CRAN-shiny 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-uuid 

%description
A no-frills open-source solution for designing plot labels affixed with QR
codes. It features 'EasyQrlabelr', a 'BrAPI-compliant' 'shiny' app that
simplifies the process of plot label design for non-R users. It builds on
the methods described by Wu 'et al.' (2020) <doi:10.1111/2041-210X.13405>.

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
