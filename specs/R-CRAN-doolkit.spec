%global __brp_check_rpaths %{nil}
%global packname  doolkit
%global packver   1.42.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.42.1
Release:          1%{?dist}%{?buildtag}
Summary:          Exploration of Dental Surface Topography

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Morpho 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-Rvcg 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-tis 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-concaveman 
BuildRequires:    R-CRAN-usethis 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Morpho 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-Rvcg 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-tis 
Requires:         R-methods 
Requires:         R-CRAN-concaveman 
Requires:         R-CRAN-usethis 

%description
Tools for exploring the topography of 3d triangle meshes. The functions
were developed with dental surfaces in mind, but could be applied to any
triangle mesh of class 'mesh3d'. More specifically, 'doolkit' allows to
isolate the border of a mesh, or a subpart of the mesh using the polygon
networks method; crop a mesh; compute basic descriptors (elevation,
orientation, footprint area); compute slope, angularity and relief index
(Ungar and Williamson (2000)
<https://palaeo-electronica.org/2000_1/gorilla/issue1_00.htm>; Boyer
(2008) <doi:10.1016/j.jhevol.2008.08.002>), inclination and occlusal
relief index or gamma (Guy et al. (2013)
<doi:10.1371/journal.pone.0066142>), OPC (Evans et al. (2007)
<doi:10.1038/nature05433>), OPCR (Wilson et al. (2012)
<doi:10.1038/nature10880>), DNE (Bunn et al. (2011)
<doi:10.1002/ajpa.21489>; Pampush et al. (2016)
<doi:10.1007/s10914-016-9326-0>), form factor (Horton (1932)
<doi:10.1029/TR013i001p00350>), basin elongation (Schum (1956)
<doi:10.1130/0016-7606(1956)67[597:EODSAS]2.0.CO;2>), lemniscate ratio
(Chorley et al; (1957) <doi:10.2475/ajs.255.2.138>), enamel-dentine
distance (Guy et al. (2015) <doi:10.1371/journal.pone.0138802>; Thiery et
al. (2017) <doi:10.3389/fphys.2017.00524>), absolute crown strength
(Schwartz et al. (2020) <doi:10.1098/rsbl.2019.0671>), relief rate (Thiery
et al. (2019) <doi:10.1002/ajpa.23916>) and area-relative curvature; draw
cumulative profiles of a topographic variable; and map a variable over a
3d triangle mesh.

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
