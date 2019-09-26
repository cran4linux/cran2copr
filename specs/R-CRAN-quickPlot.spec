%global packname  quickPlot
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          A System of Plotting Optimized for Speed and Modularity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-fpCompare 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridBase 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-backports 
Requires:         R-CRAN-fpCompare 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-gridBase 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-sp 
Requires:         R-stats 

%description
A high-level plotting system, built using 'grid' graphics, that is
optimized for speed and modularity. This has great utility for quick
visualizations when testing code, with the key benefit that visualizations
are updated independently of one another.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/maps
%{rlibdir}/%{packname}/INDEX
