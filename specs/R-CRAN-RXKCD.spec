%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RXKCD
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Get XKCD Comic from R

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-duckdb 
BuildRequires:    R-CRAN-text2vec 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-png 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-duckdb 
Requires:         R-CRAN-text2vec 

%description
Visualize your favorite XKCD comic strip directly from R. Includes
full-text search with BM25 ranking and semantic similarity search via
local 'GloVe' embeddings, powered by a local 'DuckDB' cache.

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
