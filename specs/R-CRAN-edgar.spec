%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  edgar
%global packver   2.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Tool for the U.S. SEC EDGAR Retrieval and Parsing of Corporate Filings

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-qdapRegex 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-qdapRegex 
Requires:         R-CRAN-httr 

%description
In the USA, companies file different forms with the U.S. Securities and
Exchange Commission (SEC) through EDGAR (Electronic Data Gathering,
Analysis, and Retrieval system). The EDGAR database automated system
collects all the different necessary filings and makes it publicly
available. This package facilitates retrieving, storing, searching, and
parsing of all the available filings on the EDGAR server. It downloads
filings from SEC server in bulk with a single query. Additionally, it
provides various useful functions: extracts 8-K triggering events, extract
"Business (Item 1)" and "Management's Discussion and Analysis(Item 7)"
sections of annual statements, searches filings for desired keywords,
provides sentiment measures, parses filing header information, and
provides HTML view of SEC filings.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
