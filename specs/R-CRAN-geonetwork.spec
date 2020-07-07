%global packname  geonetwork
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}
Summary:          Geographic Networks

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 

%description
Provides classes and methods for handling networks or graphs whose nodes
are geographical (i.e. locations in the globe). The functionality includes
the creation of objects of class geonetwork as a graph with node
coordinates, the computation of network measures, the support of spatial
operations (projection to different Coordinate Reference Systems, handling
of bounding boxes, etc.) and the plotting of the geonetwork object
combined with supplementary cartography for spatial representation.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
