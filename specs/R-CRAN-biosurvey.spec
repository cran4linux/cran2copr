%global __brp_check_rpaths %{nil}
%global packname  biosurvey
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Biological Survey Planning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-maps >= 3.3
BuildRequires:    R-CRAN-raster >= 3.0
BuildRequires:    R-CRAN-vegan >= 2.5
BuildRequires:    R-CRAN-picante >= 1.8
BuildRequires:    R-CRAN-spatstat.geom >= 1.65
BuildRequires:    R-CRAN-foreach >= 1.5
BuildRequires:    R-CRAN-rgdal >= 1.4
BuildRequires:    R-CRAN-sp >= 1.3
BuildRequires:    R-CRAN-ks >= 1.11
BuildRequires:    R-CRAN-doParallel >= 1.0
BuildRequires:    R-CRAN-diptest >= 0.75
BuildRequires:    R-CRAN-rgeos >= 0.5
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-maps >= 3.3
Requires:         R-CRAN-raster >= 3.0
Requires:         R-CRAN-vegan >= 2.5
Requires:         R-CRAN-picante >= 1.8
Requires:         R-CRAN-spatstat.geom >= 1.65
Requires:         R-CRAN-foreach >= 1.5
Requires:         R-CRAN-rgdal >= 1.4
Requires:         R-CRAN-sp >= 1.3
Requires:         R-CRAN-ks >= 1.11
Requires:         R-CRAN-doParallel >= 1.0
Requires:         R-CRAN-diptest >= 0.75
Requires:         R-CRAN-rgeos >= 0.5
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
A collection of tools that allows users to plan systems of sampling sites,
increasing the efficiency of biodiversity monitoring by considering the
relationship between environmental and geographic conditions in a region.
The options for selecting sampling sites included here differ from other
implementations in that they consider the environmental and geographic
conditions of a region to suggest sampling sites that could increase the
efficiency of efforts dedicated to monitoring biodiversity. The methods
proposed here are new in the sense that they combine various criteria and
points previously made in related literature; some of the theoretical and
methodological bases considered are described in: Arita et al. (2011)
<doi:10.1111/j.1466-8238.2011.00662.x>, Soberón and Cavner (2015)
<doi:10.17161/bi.v10i0.4801>, and Soberón et al. (2021).

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
