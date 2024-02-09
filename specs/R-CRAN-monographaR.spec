%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  monographaR
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Taxonomic Monographs Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-png 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-terra 

%description
Contains functions intended to facilitate the production of plant
taxonomic monographs. The package includes functions to convert tables
into taxonomic descriptions, lists of collectors, examined specimens,
identification keys (dichotomous and interactive), and can generate a
monograph skeleton. Additionally, wrapper functions to batch the
production of phenology histograms and distributional and diversity maps
are also available.

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
