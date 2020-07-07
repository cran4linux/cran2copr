%global packname  geojsonio
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          3%{?dist}
Summary:          Convert Data from and to 'GeoJSON' or 'TopoJSON'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 0.9.21
BuildRequires:    R-CRAN-sf >= 0.6
BuildRequires:    R-CRAN-readr >= 0.2.2
BuildRequires:    R-CRAN-geojson >= 0.2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-V8 
BuildRequires:    R-CRAN-jqr 
Requires:         R-CRAN-jsonlite >= 0.9.21
Requires:         R-CRAN-sf >= 0.6
Requires:         R-CRAN-readr >= 0.2.2
Requires:         R-CRAN-geojson >= 0.2.0
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-crul 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-V8 
Requires:         R-CRAN-jqr 

%description
Convert data to 'GeoJSON' or 'TopoJSON' from various R classes, including
vectors, lists, data frames, shape files, and spatial classes. 'geojsonio'
does not aim to replace packages like 'sp', 'rgdal', 'rgeos', but rather
aims to be a high level client to simplify conversions of data from and to
'GeoJSON' and 'TopoJSON'.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/js
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX
