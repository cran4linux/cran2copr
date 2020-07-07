%global packname  RSelenium
%global packver   1.7.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.7
Release:          3%{?dist}
Summary:          R Bindings for 'Selenium WebDriver'

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-wdman >= 0.2.2
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-binman 
Requires:         R-CRAN-wdman >= 0.2.2
Requires:         R-CRAN-XML 
Requires:         R-methods 
Requires:         R-CRAN-caTools 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-binman 

%description
Provides a set of R bindings for the 'Selenium 2.0 WebDriver' (see
<https://selenium.dev/documentation/en/> for more information) using the
'JsonWireProtocol' (see
<https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol> for more
information). 'Selenium 2.0 WebDriver' allows driving a web browser
natively as a user would either locally or on a remote machine using the
Selenium server it marks a leap forward in terms of web browser
automation. Selenium automates web browsers (commonly referred to as
browsers). Using RSelenium you can automate browsers locally or remotely.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/apps
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/sauceTests
%{rlibdir}/%{packname}/INDEX
