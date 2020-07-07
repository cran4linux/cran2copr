%global packname  AnimalHabitatNetwork
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Networks Characterising the Physical Configurations of AnimalHabitats

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


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
