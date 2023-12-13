%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adbcpostgresql
%global packver   0.8.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          'Arrow' Database Connectivity ('ADBC') 'PostgreSQL' Driver

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-adbcdrivermanager 
Requires:         R-CRAN-adbcdrivermanager 

%description
Provides a developer-facing interface to the 'Arrow' Database Connectivity
('ADBC') 'PostgreSQL' driver for the purposes of building high-level
database interfaces for users. 'ADBC' <https://arrow.apache.org/adbc/> is
an API standard for database access libraries that uses 'Arrow' for result
sets and query parameters.

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
