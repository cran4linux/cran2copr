%global __brp_check_rpaths %{nil}
%global packname  spnet
%global packver   0.9.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Plotting (Social) Networks on Maps

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-shape 
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-shape 

%description
Facilitates the rendering of networks for which nodes have a specific
position on a map (cities, participants in a political debate, etc.). Map
data and network data are stored together in a single object which handles
the match between network nodes and their respective position on the map.
The plot method renders both the map and the network data. Several
networks can be plot simultaneously. The graphic is highly customisable
and the legend is automatically printed. Map data have to be supplied as
'SpatialPolygons' objects (from the 'sp' package) and network data as
'named matrix'.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
