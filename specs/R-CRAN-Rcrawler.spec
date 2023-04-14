%global __brp_check_rpaths %{nil}
%global packname  Rcrawler
%global packver   0.1.9-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9.1
Release:          3%{?dist}%{?buildtag}
Summary:          Web Crawler and Scraper

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-selectr 
BuildRequires:    R-CRAN-webdriver 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-selectr 
Requires:         R-CRAN-webdriver 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-jsonlite 

%description
Performs parallel web crawling and web scraping. It is designed to crawl,
parse and store web pages to produce data that can be directly used for
analysis application. For details see Khalil and Fakir (2017)
<DOI:10.1016/j.softx.2017.04.004>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
