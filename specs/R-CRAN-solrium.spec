%global __brp_check_rpaths %{nil}
%global packname  solrium
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          General Purpose R Interface to 'Solr'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-xml2 >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-crul >= 0.4.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-jsonlite >= 1.0
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-crul >= 0.4.0
Requires:         R-utils 
Requires:         R-CRAN-R6 

%description
Provides a set of functions for querying and parsing data from 'Solr'
(<https://solr.apache.org/>) 'endpoints' (local and remote), including
search, 'faceting', 'highlighting', 'stats', and 'more like this'. In
addition, some functionality is included for creating, deleting, and
updating documents in a 'Solr' 'database'.

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
