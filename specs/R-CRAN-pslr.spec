%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pslr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Public Suffix List Engine

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-punycoder >= 1.1.0
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-punycoder >= 1.1.0
Requires:         R-tools 
Requires:         R-utils 

%description
A focused implementation of the Public Suffix List (PSL). Bundles a
reproducible, pinned PSL snapshot and implements the official
prevailing-rule algorithm to answer public-suffix (eTLD) and
registrable-domain (eTLD+1) queries. Distinguishes ICANN and PRIVATE rule
sections, accepts Unicode and ASCII hostnames via 'punycoder'
canonicalization, and supports an explicit, validated offline refresh
path. The matcher is compiled with 'cpp11' and requires no external system
library.

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
