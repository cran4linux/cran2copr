%global packname  rmapshaper
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          3%{?dist}
Summary:          Client for 'mapshaper' for 'Geospatial' Operations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-V8 >= 3.0
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-sp >= 1.2.7
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-geojsonio >= 0.6.0
BuildRequires:    R-CRAN-sf >= 0.6
BuildRequires:    R-CRAN-geojsonlint >= 0.2.0
BuildRequires:    R-methods 
Requires:         R-CRAN-V8 >= 3.0
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-sp >= 1.2.7
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-geojsonio >= 0.6.0
Requires:         R-CRAN-sf >= 0.6
Requires:         R-CRAN-geojsonlint >= 0.2.0
Requires:         R-methods 

%description
Edit and simplify 'geojson', 'Spatial', and 'sf' objects.  This is wrapper
around the 'mapshaper' 'JavaScript' library by Matthew Bloch
<https://github.com/mbloch/mapshaper/> to perform topologically-aware
polygon simplification, as well as other operations such as clipping,
erasing, dissolving, and converting 'multi-part' to 'single-part'
geometries.  It relies on the 'geojsonio' package for working with
'geojson' objects, the 'sf' package for working with 'sf' objects, and the
'sp' and 'rgdal' packages for working with 'Spatial' objects.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/mapshaper
%{rlibdir}/%{packname}/INDEX
