%global packname  leafpm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Leaflet Map Plugin for Drawing and Editing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet >= 2.0.1
BuildRequires:    R-CRAN-sf >= 0.5.2
BuildRequires:    R-CRAN-htmltools >= 0.3
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-leaflet >= 2.0.1
Requires:         R-CRAN-sf >= 0.5.2
Requires:         R-CRAN-htmltools >= 0.3
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-jsonlite 

%description
A collection of tools for interactive manipulation of (spatial) data
layers on leaflet web maps. Tools include editing of existing layers,
creation of new layers through drawing of shapes (points, lines,
polygons), deletion of shapes as well as cutting holes into existing
shapes. Provides control over options to e.g. prevent self-intersection of
polygons and lines or to enable/disable snapping to align shapes.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
