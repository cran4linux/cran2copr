%global packname  rgbif
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Interface to the Global 'Biodiversity' Information Facility API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-crul >= 0.7.4
BuildRequires:    R-CRAN-wicket >= 0.4.0
BuildRequires:    R-CRAN-oai >= 0.2.2
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-geoaxe 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-lazyeval 
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-crul >= 0.7.4
Requires:         R-CRAN-wicket >= 0.4.0
Requires:         R-CRAN-oai >= 0.2.2
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-geoaxe 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-lazyeval 

%description
A programmatic interface to the Web Service methods provided by the Global
Biodiversity Information Facility ('GBIF';
<https://www.gbif.org/developer/summary>). 'GBIF' is a database of species
occurrence records from sources all over the globe. 'rgbif' includes
functions for searching for taxonomic names, retrieving information on
data providers, getting species occurrence records, getting counts of
occurrence records, and using the 'GBIF' tile map service to make
'rasters' summarizing huge amounts of data.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/assets
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/singlemaplayout.html
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX
