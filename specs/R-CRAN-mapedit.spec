%global packname  mapedit
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Interactive Editing of Spatial Data in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet >= 2.0.1
BuildRequires:    R-CRAN-leaflet.extras >= 1.0
BuildRequires:    R-CRAN-sf >= 0.5.2
BuildRequires:    R-CRAN-htmltools >= 0.3
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-leafpm 
BuildRequires:    R-CRAN-mapview 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-leaflet >= 2.0.1
Requires:         R-CRAN-leaflet.extras >= 1.0
Requires:         R-CRAN-sf >= 0.5.2
Requires:         R-CRAN-htmltools >= 0.3
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-leafpm 
Requires:         R-CRAN-mapview 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-shiny 

%description
Suite of interactive functions and helpers for selecting and editing
geospatial data.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/posts
%{rlibdir}/%{packname}/INDEX
