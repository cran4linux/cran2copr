%global packname  LST
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Land Surface Temperature Retrieval

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
Requires:         R-CRAN-raster 

%description
Calculates Land Surface Temperature from Landsat band 10 and 11. Land
surface temperature retrieval from LANDSAT TM 5. Sobrino JA, Jiménez-Muñoz
JC, Paolini L (2004). <doi:10.1016/j.rse.2004.02.003>. Mapping land
surface emissivity from NDVI: Application to European, African, and South
American areas. Valor E (1996). <doi:10.1016/0034-4257(96)00039-9>. On the
relationship between thermal emissivity and the normalized difference
vegetation index for natural surfaces. Van de Griend AA, Owe M (1993).
<doi:10.1080/01431169308904400>.

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
