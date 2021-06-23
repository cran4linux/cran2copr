%global __brp_check_rpaths %{nil}
%global packname  od
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Manipulate and Map Origin-Destination Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sfheaders 
BuildRequires:    R-methods 
Requires:         R-CRAN-sfheaders 
Requires:         R-methods 

%description
The aim of 'od' is to provide tools and example datasets for working with
origin-destination ('OD') datasets of the type used to describe aggregate
urban mobility patterns (Carey et al. 1981) <doi:10.1287/trsc.15.1.32>.
The package builds on functions for working with 'OD' data in the package
'stplanr', (Lovelace and Ellison 2018) <doi:10.32614/RJ-2018-053> with a
focus on computational efficiency and support for the 'sf' class system
(Pebesma 2018) <doi:10.32614/RJ-2018-009>. With few dependencies and a
simple class system based on data frames, the package is intended to
facilitate efficient analysis of 'OD' datasets and to provide a place for
developing new functions. The package enables the creation and analysis of
geographic entities representing large scale mobility patterns, from daily
travel between zones in cities to migration between countries.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
