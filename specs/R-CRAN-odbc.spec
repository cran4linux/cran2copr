%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  odbc
%global packver   1.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          Connect to ODBC Compatible Databases (using the DBI Interface)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    unixODBC-devel
BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-blob >= 1.2.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-DBI >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-methods 
Requires:         R-CRAN-blob >= 1.2.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-DBI >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-lifecycle 
Requires:         R-methods 

%description
A DBI-compatible interface to ODBC databases.

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
