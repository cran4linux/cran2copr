%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sapo
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Association of Different Types of Polygon

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-sf 
Requires:         R-methods 
Requires:         R-stats 

%description
In ecology, spatial data is often represented using polygons. These
polygons can represent a variety of spatial entities, such as ecological
patches, animal home ranges, or gaps in the forest canopy.  Researchers
often need to determine if two spatial processes, represented by these
polygons, are independent of each other. For instance, they might want to
test if the home range of a particular animal species is influenced by the
presence of a certain type of vegetation.  To address this, Godoy et al.
(2022) (<doi:10.1016/j.spasta.2022.100695>) developed conditional Monte
Carlo tests. These tests are designed to assess spatial independence while
taking into account the shape and size of the polygons.

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
