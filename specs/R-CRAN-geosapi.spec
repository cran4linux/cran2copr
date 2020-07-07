%global packname  geosapi
%global packver   0.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          3%{?dist}
Summary:          GeoServer REST API R Interface

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-XML 

%description
Provides an R interface to the GeoServer REST API, allowing to upload and
publish data in a GeoServer web-application and expose data to OGC
Web-Services. The package currently supports all CRUD
(Create,Read,Update,Delete) operations on GeoServer workspaces,
namespaces, datastores (stores of vector data), featuretypes, layers,
styles, as well as vector data upload operations. For more information
about the GeoServer REST API, see
<http://docs.geoserver.org/stable/en/user/rest/>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
