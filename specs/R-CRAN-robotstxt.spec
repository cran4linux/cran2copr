%global packname  robotstxt
%global packver   0.7.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.4
Release:          2%{?dist}
Summary:          A 'robots.txt' Parser and 'Webbot'/'Spider'/'Crawler'Permissions Checker

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-future >= 1.6.2
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-future.apply >= 1.0.0
BuildRequires:    R-CRAN-spiderbar >= 0.2.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
Requires:         R-CRAN-future >= 1.6.2
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-future.apply >= 1.0.0
Requires:         R-CRAN-spiderbar >= 0.2.0
Requires:         R-CRAN-magrittr 
Requires:         R-utils 

%description
Provides functions to download and parse 'robots.txt' files. Ultimately
the package makes it easy to check if bots (spiders, crawler, scrapers,
...) are allowed to access specific resources on a domain.

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
%doc %{rlibdir}/%{packname}/http_requests
%doc %{rlibdir}/%{packname}/robotstxts
%doc %{rlibdir}/%{packname}/urls.txt
%{rlibdir}/%{packname}/INDEX
