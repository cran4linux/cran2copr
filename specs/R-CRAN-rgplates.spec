%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rgplates
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface for the GPlates Web Service and Desktop Application

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-sf 
Requires:         R-methods 
Requires:         R-utils 

%description
Query functions to the GPlates <https://www.gplates.org/> Desktop
Application and the GPlates Web Service <https://gws.gplates.org/> allow
users to reconstruct past positions of geographic entities based on
user-selected rotation models without leaving the R running environment.
The online method (GPlates Web Service) makes the rotation of static
plates, coastlines, and a low number of geographic coordinates available
using nothing but an internet connection. The offline method requires an
external installation of the GPlates Desktop Application, but allows the
efficient batch rotation of thousands of coordinates, Simple Features (sf)
and Spatial (sp) objects with custom reconstruction trees and partitioning
polygons. Examples of such plate tectonic models are accessible via the
chronosphere <https://cran.r-project.org/package=chronosphere>. This R
extension is developed under the umbrella of the DFG (Deutsche
Forschungsgemeinschaft) Research Unit TERSANE2 (For 2332, TEmperature
Related Stressors in ANcient Extinctions).

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
