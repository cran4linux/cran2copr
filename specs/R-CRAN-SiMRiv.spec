%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SiMRiv
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Simulating Multistate Movements in River/Heterogeneous Landscapes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-mco 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-CRAN-raster 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-mco 
Requires:         R-parallel 
Requires:         R-CRAN-rgdal 

%description
Provides functions to generate and analyze spatially-explicit
individual-based multistate movements in rivers, heterogeneous and
homogeneous spaces. This is done by incorporating landscape bias on local
behaviour, based on resistance rasters. Although originally conceived and
designed to simulate trajectories of species constrained to linear
habitats/dendritic ecological networks (e.g. river networks), the
simulation algorithm is built to be highly flexible and can be applied to
any (aquatic, semi-aquatic or terrestrial) organism, independently on the
landscape in which it moves. Thus, the user will be able to use the
package to simulate movements either in homogeneous landscapes,
heterogeneous landscapes (e.g. semi-aquatic animal moving mainly along
rivers but also using the matrix), or even in highly contrasted landscapes
(e.g. fish in a river network). The algorithm and its input parameters are
the same for all cases, so that results are comparable. Simulated
trajectories can then be used as mechanistic null models (Potts & Lewis
2014, <DOI:10.1098/rspb.2014.0231>) to test a variety of 'Movement
Ecology' hypotheses (Nathan et al. 2008, <DOI:10.1073/pnas.0800375105>),
including landscape effects (e.g. resources, infrastructures) on animal
movement and species site fidelity, or for predictive purposes (e.g. road
mortality risk, dispersal/connectivity). The package should be relevant to
explore a broad spectrum of ecological phenomena, such as those at the
interface of animal behaviour, management, landscape and movement ecology,
disease and invasive species spread, and population dynamics.

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
