%global packname  tmap
%global packver   2.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.2
Release:          1%{?dist}
Summary:          Thematic Maps

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.7.15
BuildRequires:    R-CRAN-tmaptools >= 2.0.2
BuildRequires:    R-CRAN-leaflet >= 2.0.2
BuildRequires:    R-CRAN-sf >= 0.7.1
BuildRequires:    R-CRAN-units >= 0.6.1
BuildRequires:    R-CRAN-lwgeom >= 0.1.4
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-leafsync 
BuildRequires:    R-stats 
Requires:         R-CRAN-raster >= 2.7.15
Requires:         R-CRAN-tmaptools >= 2.0.2
Requires:         R-CRAN-leaflet >= 2.0.2
Requires:         R-CRAN-sf >= 0.7.1
Requires:         R-CRAN-units >= 0.6.1
Requires:         R-CRAN-lwgeom >= 0.1.4
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-leafsync 
Requires:         R-stats 

%description
Thematic maps are geographical maps in which spatial data distributions
are visualized. This package offers a flexible, layer-based, and easy to
use approach to create thematic maps, such as choropleths and bubble maps.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/tips.txt
%{rlibdir}/%{packname}/INDEX
