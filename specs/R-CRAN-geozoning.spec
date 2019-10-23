%global packname  geozoning
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Zoning Methods for Spatial Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-RandomFields 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-RandomFields 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-raster 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-ggplot2 

%description
A zoning method and a numerical criterion for zoning quality are available
in this package. The zoning method is based on a numerical criterion that
evaluates the zoning quality. This criterion quantifies simultaneously how
zones are heterogeneous on the whole map and how neighbouring zones are
similar. This approach allows comparison between maps either with
different zones or different labels, which is of importance for zone
delineation algorithms aiming at maximizing inter-zone variability. An
optimisation procedure provides the user with the best zonings thanks to
contour delineation for a given map.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
