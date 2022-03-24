%global __brp_check_rpaths %{nil}
%global packname  timeseriesdb
%global packver   1.0.0-1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Time Series Database for Official Statistics with R and PostgreSQL

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.4
BuildRequires:    R-CRAN-RPostgres >= 1.2.0
BuildRequires:    R-CRAN-jsonlite >= 1.1
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-DBI 
Requires:         R-CRAN-data.table >= 1.9.4
Requires:         R-CRAN-RPostgres >= 1.2.0
Requires:         R-CRAN-jsonlite >= 1.1
Requires:         R-utils 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-DBI 

%description
Archive and manage times series data from official statistics. The
'timeseriesdb' package was designed to manage a large catalog of time
series from official statistics which are typically published on a
monthly, quarterly or yearly basis. Thus timeseriesdb is optimized to
handle updates caused by data revision as well as elaborate, multi-lingual
meta information.

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
