%global __brp_check_rpaths %{nil}
%global packname  codemetar
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generate 'CodeMeta' Metadata for R Packages

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-commonmark 
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-gert 
BuildRequires:    R-CRAN-gh 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pingr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-sessioninfo 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-commonmark 
Requires:         R-CRAN-crul 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-gert 
Requires:         R-CRAN-gh 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-memoise 
Requires:         R-methods 
Requires:         R-CRAN-pingr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-sessioninfo 
Requires:         R-stats 
Requires:         R-CRAN-urltools 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-cli 

%description
The 'Codemeta' Project defines a 'JSON-LD' format for describing software
metadata, as detailed at <https://codemeta.github.io>. This package
provides utilities to generate, parse, and modify 'codemeta.json' files
automatically for R packages, as well as tools and examples for working
with 'codemeta.json' 'JSON-LD' more generally.

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
