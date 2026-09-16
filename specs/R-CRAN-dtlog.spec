%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dtlog
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Logging for 'data.table' Operations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-stats 
Requires:         R-utils 

%description
Provides feedback about 'data.table' operations. 'dtlog' redefines the
subsetting method for data tables as well as several functions exported by
'data.table' so that each operation prints a short message describing what
it did: how many rows were removed, which columns were added, updated or
dropped, how many groups an aggregation produced, and so on. The
operations themselves are left untouched, including modification by
reference. It also provides dttable(), which describes the variables a
single data table holds and passes every other call on to base::table()
unchanged. Inspired by the 'tidylog' package.

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
