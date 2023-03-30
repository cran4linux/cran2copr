%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  polmineR
%global packver   0.8.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.8
Release:          1%{?dist}%{?buildtag}
Summary:          Verbs and Nouns for Corpus Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.12.2
BuildRequires:    R-CRAN-RcppCWB >= 0.5.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-RcppCWB >= 0.5.3
Requires:         R-methods 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-stringi 
Requires:         R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-cli 

%description
Package for corpus analysis using the Corpus Workbench ('CWB',
<https://cwb.sourceforge.io>) as an efficient back end for indexing and
querying large corpora. The package offers functionality to flexibly
create subcorpora and to carry out basic statistical operations (count,
co-occurrences etc.). The original full text of documents can be
reconstructed and inspected at any time. Beyond that, the package is
intended to serve as an interface to packages implementing advanced
statistical procedures. Respective data structures (document-term
matrices, term-co-occurrence matrices etc.) can be created based on the
indexed corpora.

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
