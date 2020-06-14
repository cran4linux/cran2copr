%global packname  loa
%global packver   0.2.45.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.45.4
Release:          2%{?dist}
Summary:          Lattice Options and Add-Ins

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-RgoogleMaps 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-plyr 
Requires:         R-lattice 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-grid 
Requires:         R-CRAN-png 
Requires:         R-CRAN-RgoogleMaps 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-mgcv 
Requires:         R-CRAN-plyr 

%description
Various plots and functions that make use of the lattice/trellis plotting
framework. The plots, which include loaPlot(), RgoogleMapsPlot() and
trianglePlot(), use panelPal(), a function that extends 'lattice' and
'hexbin' package methods to automate plot subscript and panel-to-panel and
panel-to-key synchronization/management.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
