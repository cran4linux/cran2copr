%global __brp_check_rpaths %{nil}
%global packname  rgplates
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface for the GPlates Web Service and Desktop Application

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-utils 
Requires:         R-CRAN-sp 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-CRAN-rgdal 
Requires:         R-utils 

%description
Query functions to the GPlates <https://www.gplates.org/> desktop
application and the GPlates Web Service <https://gws.gplates.org/> allow
users to reconstruct coordinates, static plates, and Spatial objects
without leaving the R running environment. This R extension was supported
by the FAU GeoZentrum Nordbayern and is developed under the umbrella of
the DFG (Deutsche Forschungsgemeinschaft) Research Unit TERSANE2 (For
2332, TEmperature Related Stressors in ANcient Extinctions).

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
