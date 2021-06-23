%global __brp_check_rpaths %{nil}
%global packname  rotl
%global packver   3.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.11
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the 'Open Tree of Life' API

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rncl >= 0.6.0
BuildRequires:    R-CRAN-assertthat >= 0.1
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rentrez 
Requires:         R-CRAN-rncl >= 0.6.0
Requires:         R-CRAN-assertthat >= 0.1
Requires:         R-CRAN-ape 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rentrez 

%description
An interface to the 'Open Tree of Life' API to retrieve phylogenetic
trees, information about studies used to assemble the synthetic tree, and
utilities to match taxonomic names to 'Open Tree identifiers'. The 'Open
Tree of Life' aims at assembling a comprehensive phylogenetic tree for all
named species.

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
