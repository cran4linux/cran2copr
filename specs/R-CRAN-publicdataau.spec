%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  publicdataau
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Australian Government Open Data from 'publicdata.au'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 

%description
Search, filter, total and download the Australian government open data
republished at <https://publicdata.au/>, where every version of a dataset
is kept at a URL that never changes. Rows and totals come from the site's
query API as typed, labelled 'tibble' data frames, and whole tables from
its files in any of twelve formats. Map layers come as 'sf' objects, and
rows that carry the code of an area join to the Australian Bureau of
Statistics boundaries in one call. The 'DuckDB' file of any version can be
attached over the web and queried in place with 'DBI' or 'dplyr'.
Downloads can be kept in a cache, since a version never changes, the
changes between versions are listed row by row, and the source file, fetch
time and checksum of every version are on record. Every answer carries the
version it came from and the attribution the publisher's licence requires,
and citations come as 'BibTeX'. Any dataset the site serves works by its
slug, so a new dataset needs no new release.

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
