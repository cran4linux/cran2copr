%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  secfile
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          SEC 'EDGAR' APIs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-xml2 

%description
Simple and efficient access to the SEC's 'EDGAR' APIs
<https://www.sec.gov/search-filings> for querying and retrieving filings.
The 'secfile' package abstracts the complexities of interacting with SEC
EDGAR APIs, such as session management, user agent declaration, rate
limiting, index parsing, pagination of filing metadata, URL construction,
document caching, and inline XBRL parsing. This abstraction allows users
to focus on retrieving data rather than managing API details. Use cases
include retrieving filings across a range of workflows such as indexes,
tenures, submissions, and facts. The package supports flexible query
capabilities, including customizable form types, date ranges, and
dimensions, and automatic data validation. It handles the SEC's fair
access requirements automatically, such as user agent declaration and rate
limiting between requests, and caches downloaded documents for efficient
retrieval of large datasets. The implementation uses standard HTTP
libraries to handle API interactions efficiently and is available in both
R and 'Python' for accessibility to a broad audience.

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
