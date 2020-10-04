%global packname  ZillowR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          R Interface to Zillow Real Estate and Mortgage Data API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-XML 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-XML 

%description
Zillow, an online real estate company, provides real estate and mortgage
data for the United States through a REST API. The ZillowR package
provides an R function for each API service, making it easy to make API
calls and process the response into convenient, R-friendly data
structures. See <http://www.zillow.com/howto/api/APIOverview.htm> for the
Zillow API Documentation.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/xml_response_examples
%doc %{rlibdir}/%{packname}/xml_schemas
%{rlibdir}/%{packname}/INDEX
