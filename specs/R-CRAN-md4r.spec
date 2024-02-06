%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  md4r
%global packver   0.5.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Markdown Parser Implemented using the 'MD4C' Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-textutils 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-textutils 
Requires:         R-CRAN-stringr 

%description
Provides an R wrapper for the 'MD4C' (Markdown for 'C') library. Functions
exist for parsing markdown ('CommonMark' compliant) along with support for
other common markdown extensions (e.g. GitHub flavored markdown, 'LaTeX'
equation support, etc.). The package also provides a number of higher
level functions for exploring and manipulating markdown abstract syntax
trees as well as translating and displaying the documents.

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
