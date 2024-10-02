%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AnimalHabitatNetwork
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Networks Characterising the Physical Configurations of Animal Habitats

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-igraph >= 1.2.4.1
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-igraph >= 1.2.4.1
Requires:         R-stats 

%description
Functions for generating and visualising networks for characterising the
physical attributes and spatial organisations of habitat components (i.e.
habitat physical configurations). The network generating algorithm first
determines the X and Y coordinates of N nodes within a rectangle with a
side length of L and an area of A. Then it computes the pair-wise
Euclidean distance Dij between node i and j, and then a complete network
with 1/Dij as link weights is constructed. Then, the algorithm removes
links from the complete network with the probability as shown in the
function ahn_prob(). Such link removals can make the network disconnected
whereas a connected network is wanted. In such cases, the algorithm
rewires one network component to its spatially nearest neighbouring
component and repeat doing this until the network is connected again.
Finally, it outputs an undirected network (weighted or unweighted,
connected or disconnected). This package came with a manuscript on
modelling the physical configurations of animal habitats using networks
(in preparation).

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
