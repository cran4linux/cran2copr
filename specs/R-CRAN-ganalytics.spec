%global packname  ganalytics
%global packver   0.10.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.7
Release:          3%{?dist}
Summary:          Interact with 'Google Analytics'

License:          MIT + file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-stringr >= 1.0
BuildRequires:    R-CRAN-googleAnalyticsR >= 0.6.0
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-selectr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-stringr >= 1.0
Requires:         R-CRAN-googleAnalyticsR >= 0.6.0
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-selectr 
Requires:         R-CRAN-tibble 

%description
Functions for querying the 'Google Analytics' core reporting, real-time,
multi-channel funnel and management APIs, as well as the 'Google Tag
Manager' (GTM) API. Write methods are also provided for the management and
GTM APIs so that you can change tag, property or view settings, for
example. Define reporting queries using natural R expressions instead of
being concerned as much about API technical intricacies like query syntax,
character code escaping, and API limitations.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/figures
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
