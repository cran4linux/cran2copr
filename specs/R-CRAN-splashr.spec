%global packname  splashr
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}
Summary:          Tools to Work with the 'Splash' 'JavaScript' Rendering andScraping Service

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stevedore 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-formatR 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-HARtools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-stevedore 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-formatR 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-HARtools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 

%description
'Splash' <https://github.com/scrapinghub/splash> is a 'JavaScript'
rendering service. It is a lightweight web browser with an 'HTTP' API,
implemented in 'Python' using 'Twisted' and 'QT' and provides some of the
core functionality of the 'RSelenium' or 'seleniumPipes' R packages in a
lightweight footprint. Some of 'Splash' features include the ability to
process multiple web pages in parallel; retrieving 'HTML' results and/or
take screen shots; disabling images or use 'Adblock Plus' rules to make
rendering faster; executing custom 'JavaScript' in page context; getting
detailed rendering info in 'HAR' format.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
