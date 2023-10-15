%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chessboard
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Create Network Connections Based on Chess Moves

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tidyr 

%description
Provides functions to work with directed (asymmetric) and undirected
(symmetric) spatial networks. It makes the creation of connectivity
matrices easier, i.e. a binary matrix of dimension n x n, where n is the
number of nodes (sampling units) indicating the presence (1) or the
absence (0) of an edge (link) between pairs of nodes. Different network
objects can be produced by 'chessboard': node list, neighbor list, edge
list, connectivity matrix. It can also produce objects that will be used
later in Moran's Eigenvector Maps (Dray et al. (2006)
<doi:10.1016/j.ecolmodel.2006.02.015>) and Asymetric Eigenvector Maps
(Blanchet et al. (2008) <doi:10.1016/j.ecolmodel.2008.04.001>), methods
available in the package 'adespatial' (Dray et al. (2023)
<https://CRAN.R-project.org/package=adespatial>). This work is part of the
FRB-CESAB working group Bridge
<https://www.fondationbiodiversite.fr/en/the-frb-in-action/programs-and-projects/le-cesab/bridge/>.

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
