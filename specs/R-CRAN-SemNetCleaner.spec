%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SemNetCleaner
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Automated Cleaning Tool for Semantic and Linguistic Data

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.1
Requires:         R-core >= 4.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-SemNetDictionaries >= 0.3.0
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-hunspell 
BuildRequires:    R-CRAN-phonics 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-searcher 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringdist 
Requires:         R-CRAN-SemNetDictionaries >= 0.3.0
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-hunspell 
Requires:         R-CRAN-phonics 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-searcher 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringdist 

%description
Implements several functions that automates the cleaning and
spell-checking of text data. Also converges, finalizes, removes plurals
and continuous strings, and puts text data in binary format for semantic
network analysis. Uses the 'SemNetDictionaries' package to make the
cleaning process more accurate, efficient, and reproducible.

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
