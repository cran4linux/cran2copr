%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gfcanalysis
%global packver   1.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Working with Hansen et al. Global Forest Change Dataset

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-animation 
BuildRequires:    R-CRAN-rasterVis 
Requires:         R-CRAN-raster 
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-animation 
Requires:         R-CRAN-rasterVis 

%description
Supports analyses using the Global Forest Change dataset released by
Hansen et al. gfcanalysis was originally written for the Tropical Ecology
Assessment and Monitoring (TEAM) Network. For additional details on the
Global Forest Change dataset, see: Hansen, M. et al. 2013.
"High-Resolution Global Maps of 21st-Century Forest Cover Change." Science
342 (15 November): 850-53. The forest change data and more information on
the product is available at <http://earthenginepartners.appspot.com>.

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
