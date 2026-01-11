%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  duckspatial
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to 'DuckDB' Database with Spatial Extension

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-duckdb 
BuildRequires:    R-CRAN-geoarrow 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-wk 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-duckdb 
Requires:         R-CRAN-geoarrow 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-wk 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-lifecycle 

%description
Fast & memory-efficient functions to analyze and manipulate large spatial
data data sets. It leverages the fast analytical capabilities of 'DuckDB'
and its spatial extension (see
<https://duckdb.org/docs/stable/core_extensions/spatial/overview>) while
maintaining compatibility with R’s spatial data ecosystem to work with
spatial vector data.

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
