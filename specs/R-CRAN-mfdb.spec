%global __brp_check_rpaths %{nil}
%global packname  mfdb
%global packver   7.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          MareFrame DB Querying Library

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-RPostgres >= 1.3.0
BuildRequires:    R-CRAN-logging >= 0.7.103
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-DBI >= 0.3.1
BuildRequires:    R-CRAN-duckdb >= 0.2.5
BuildRequires:    R-CRAN-getPass >= 0.1.1
BuildRequires:    R-CRAN-RSQLite 
Requires:         R-CRAN-RPostgres >= 1.3.0
Requires:         R-CRAN-logging >= 0.7.103
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-DBI >= 0.3.1
Requires:         R-CRAN-duckdb >= 0.2.5
Requires:         R-CRAN-getPass >= 0.1.1
Requires:         R-CRAN-RSQLite 

%description
Creates and manages a PostgreSQL database suitable for storing fisheries
data and aggregating ready for use within a Gadget
<https://gadget-framework.github.io/gadget2/> model. See
<https://mareframe.github.io/mfdb/> for more information.

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
