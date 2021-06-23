%global __brp_check_rpaths %{nil}
%global packname  nightmares
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Common Analysis with Remote Sensing Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 

%description
A collection of functions used in remote sensing analysis (e.g.,
conversion from digital numbers to radiance, reflectance, and
temperature). It includes several algorithms to calculate the albedo:
Liang (2000) <doi:10.1016/S0034-4257(00)00205-4>, Silva et al. (2016)
<doi:10.32614/RJ-2016-051>, Tasumi et al. (2008)
<doi:10.1061/(ASCE)1084-0699(2008)13:2(51)>, among others; and include
functions to derive several spectral indices. Although the current version
implements basic functions, it will be expandable to a more robust tool
for water cycle modeling (e.g., to include surface runoff and
evapotranspiration calculations) in the near future. This package is under
development at the Institute about Natural Resources Research (INIRENA)
from the Universidad Michoacana de San Nicolas de Hidalgo.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
