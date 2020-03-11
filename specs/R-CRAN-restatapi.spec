%global packname  restatapi
%global packver   0.7.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.5
Release:          1%{?dist}
Summary:          Search and Retrieve Data from Eurostat Database

License:          EUPL-1.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-xml2 

%description
Eurostat is the statistical office of the European Union and provides high
quality statistics for Europe. Large set of the data is disseminated
through the Eurostat database
(<https://ec.europa.eu/eurostat/data/database>). The tools are using the
REST API with the Statistical Data and Metadata eXchange (SDMX
<https://sdmx.org>) Web Services
(<https://ec.europa.eu/eurostat/web/sdmx-web-services/about-this-service>)
to search and download data from the Eurostat database using the SDMX
standard.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
