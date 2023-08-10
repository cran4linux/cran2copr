%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geotopbricks
%global packver   1.5.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          An R Plug-in for the Distributed Hydrological Model GEOtop

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 

%description
It analyzes raster maps and other information as input/output files from
the Hydrological Distributed Model GEOtop. It contains functions and
methods to import maps and other keywords from geotop.inpts file. Some
examples with simulation cases of GEOtop 2.x/3.x are presented in the
package. Any information about the GEOtop Distributed Hydrological Model
source code is available on www.geotop.org. Technical details about the
model are available in Endrizzi et al (2014)
<https://gmd.copernicus.org/articles/7/2831/2014/gmd-7-2831-2014.html>.

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
