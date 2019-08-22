%global packname  adwordsR
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Access the 'Google Adwords' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-utils 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-rjson 
Requires:         R-utils 

%description
Allows access to selected services that are part of the 'Google Adwords'
API <https://developers.google.com/adwords/api/docs/guides/start>. 'Google
Adwords' is an online advertising service by 'Google', that delivers Ads
to users. This package offers a authentication process using 'OAUTH2'.
Currently, there are two methods of data of accessing the API, depending
on the type of request. One method uses 'SOAP' requests which require
building an 'XML' structure and then sent to the API. These are used for
the 'ManagedCustomerService' and the 'TargetingIdeaService'. The second
method is by building 'AWQL' queries for the reporting side of the 'Google
Adwords' API.

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
%{rlibdir}/%{packname}/INDEX
