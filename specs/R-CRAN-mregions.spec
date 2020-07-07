%global packname  mregions
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}
Summary:          Marine Regions Data from 'Marineregions.org'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.1.0
BuildRequires:    R-CRAN-jsonlite >= 1.0
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-wellknown 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-httr >= 1.1.0
Requires:         R-CRAN-jsonlite >= 1.0
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-wellknown 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tibble 

%description
Tools to get marine regions data from <http://www.marineregions.org/>.
Includes tools to get region metadata, as well as data in 'GeoJSON'
format, as well as Shape files. Use cases include using data downstream to
visualize 'geospatial' data by marine region, mapping variation among
different regions, and more.

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
%doc %{rlibdir}/%{packname}/ignore
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX
