%global __brp_check_rpaths %{nil}
%global packname  elastic
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          General Purpose Interface to 'Elasticsearch'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 2.2
BuildRequires:    R-CRAN-jsonlite >= 1.1
BuildRequires:    R-CRAN-crul >= 0.9.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-curl >= 2.2
Requires:         R-CRAN-jsonlite >= 1.1
Requires:         R-CRAN-crul >= 0.9.0
Requires:         R-utils 
Requires:         R-CRAN-R6 

%description
Connect to 'Elasticsearch', a 'NoSQL' database built on the 'Java' Virtual
Machine. Interacts with the 'Elasticsearch' 'HTTP' API
(<https://www.elastic.co/elasticsearch/>), including functions for setting
connection details to 'Elasticsearch' instances, loading bulk data,
searching for documents with both 'HTTP' query variables and 'JSON' based
body requests. In addition, 'elastic' provides functions for interacting
with API's for 'indices', documents, nodes, clusters, an interface to the
cat API, and more.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
