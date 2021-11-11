%global __brp_check_rpaths %{nil}
%global packname  maskRangeR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mask Species Geographic Ranges

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gdalUtils 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-virtualspecies 
Requires:         R-CRAN-gdalUtils 
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-CRAN-tidyverse 
Requires:         R-utils 
Requires:         R-CRAN-virtualspecies 

%description
Mask ranges based on expert knowledge or remote sensing layers. These
tools can be combined to quantitatively and reproducibly generate a new
map or to update an existing map. Methods include expert opinion and
data-driven tools to generate thresholds for binary masks.

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
