%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rduckhts
%global packver   0.1.3-0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3.0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          'DuckDB' High Throughput Sequencing File Formats Reader Extension

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-duckdb 
BuildRequires:    R-utils 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-duckdb 
Requires:         R-utils 

%description
Bundles the 'duckhts' 'DuckDB' extension for reading High Throughput
Sequencing file formats with 'DuckDB'. The 'DuckDB' C extension API
<https://duckdb.org/docs/stable/clients/c/api> and its 'htslib' dependency
are compiled from vendored sources during package installation. James K
Bonfield and co-authors (2021) <doi:10.1093/gigascience/giab007>.

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
