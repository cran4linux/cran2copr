%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  neonstore
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          NEON Data Store

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vroom >= 1.5.1
BuildRequires:    R-CRAN-duckdb >= 0.2.3
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-thor 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-duckdbfs 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-cachem 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-vroom >= 1.5.1
Requires:         R-CRAN-duckdb >= 0.2.3
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-thor 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-duckdbfs 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-cachem 
Requires:         R-CRAN-glue 

%description
The National Ecological Observatory Network (NEON) provides access to its
numerous data products through its REST API,
<https://data.neonscience.org/data-api/>. This package provides a
high-level user interface for downloading and storing NEON data products.
Unlike 'neonUtilities', this package will avoid repeated downloading,
provides persistent storage, and improves performance.  'neonstore' can
also construct a local 'duckdb' database of stacked tables, making it
possible to work with tables that are far to big to fit into memory.

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
