%global __brp_check_rpaths %{nil}
%global packname  rangemap
%global packver   0.1.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.17
Release:          1%{?dist}%{?buildtag}
Summary:          Simple Tools for Defining Species Ranges

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatial >= 7.3
BuildRequires:    R-CRAN-maps >= 3.3
BuildRequires:    R-CRAN-raster >= 3.0
BuildRequires:    R-CRAN-rgdal >= 1.4
BuildRequires:    R-CRAN-sp >= 1.3
BuildRequires:    R-CRAN-scales >= 1.1
BuildRequires:    R-CRAN-concaveman >= 1.0
BuildRequires:    R-CRAN-maptools >= 0.9
BuildRequires:    R-CRAN-dplyr >= 0.8
BuildRequires:    R-CRAN-sf >= 0.6
BuildRequires:    R-CRAN-rgeos >= 0.5
BuildRequires:    R-CRAN-rgl >= 0.100
BuildRequires:    R-CRAN-rnaturalearthdata >= 0.1
BuildRequires:    R-methods 
Requires:         R-CRAN-spatial >= 7.3
Requires:         R-CRAN-maps >= 3.3
Requires:         R-CRAN-raster >= 3.0
Requires:         R-CRAN-rgdal >= 1.4
Requires:         R-CRAN-sp >= 1.3
Requires:         R-CRAN-scales >= 1.1
Requires:         R-CRAN-concaveman >= 1.0
Requires:         R-CRAN-maptools >= 0.9
Requires:         R-CRAN-dplyr >= 0.8
Requires:         R-CRAN-sf >= 0.6
Requires:         R-CRAN-rgeos >= 0.5
Requires:         R-CRAN-rgl >= 0.100
Requires:         R-CRAN-rnaturalearthdata >= 0.1
Requires:         R-methods 

%description
A collection of tools to create species range maps based on occurrence
data, statistics, and spatial objects. Other tools in this collection can
be used to analyze the environmental characteristics of the species
ranges. Plotting options to represent results in various manners are also
available. Results obtained using these tools can be used to explore the
distribution of species and define areas of occupancy and extent of
occurrence of species. Other packages help to explore species
distributions using distinct methods, but options presented in this set of
tools (e.g., using trend surface analysis and concave hull polygons) are
exclusive. Description of methods, approaches, and comments for some of
the tools implemented here can be found in: IUCN (2001)
<https://portals.iucn.org/library/node/10315>, Peterson et al. (2011)
<https://www.degruyter.com/princetonup/view/title/506966>, and Graham and
Hijmans (2006) <doi:10.1111/j.1466-8238.2006.00257.x>.

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
