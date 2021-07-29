%global __brp_check_rpaths %{nil}
%global packname  stringx
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Drop-in Replacements for Base String Functions Powered by 'stringi'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringi >= 1.7.2
Requires:         R-CRAN-stringi >= 1.7.2

%description
English is the native language for only 5%% of the World population. Also,
only 17%% of us can understand this text. Moreover, the Latin alphabet is
the main one for merely 36%% of the total. The early computer era, now a
very long time ago, was dominated by the US. Due to the proliferation of
the internet, smartphones, social media, and other technologies and
communication platforms, this is no longer the case. This package replaces
base R string functions (such as grep(), tolower(), and sprintf()) with
ones that fully support the Unicode standards related to natural language
processing, fixes some long-standing inconsistencies, and introduces some
new, useful features. Thanks to 'ICU' (International Components for
Unicode) and 'stringi', they are fast, reliable, and portable across
different platforms.

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
