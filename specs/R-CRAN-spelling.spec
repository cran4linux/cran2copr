%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spelling
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Spell Checking in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-hunspell >= 3.0
BuildRequires:    R-CRAN-commonmark 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-hunspell >= 3.0
Requires:         R-CRAN-commonmark 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-knitr 

%description
Spell checking common document formats including latex, markdown, manual
pages, and description files. Includes utilities to automate checking of
documentation and vignettes as a unit test during 'R CMD check'. Both
British and American English are supported out of the box and other
languages can be added. In addition, packages may define a 'wordlist' to
allow custom terminology without having to abuse punctuation.

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
