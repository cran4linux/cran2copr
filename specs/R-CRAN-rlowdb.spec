%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rlowdb
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Lightweight JSON-Based Database

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.4
BuildRequires:    R-CRAN-R6 >= 2.5.1
BuildRequires:    R-CRAN-rlang >= 1.1.3
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-yyjsonr >= 0.1.20
Requires:         R-CRAN-cli >= 3.6.4
Requires:         R-CRAN-R6 >= 2.5.1
Requires:         R-CRAN-rlang >= 1.1.3
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-yyjsonr >= 0.1.20

%description
The goal of 'rlowdb' is to provide a lightweight, file-based JSON
database. Inspired by 'LowDB' in 'JavaScript', it generates an intuitive
interface for storing, retrieving, updating, and querying structured data
without requiring a full-fledged database system. Ideal for prototyping,
small-scale applications, and lightweight data management needs.

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
