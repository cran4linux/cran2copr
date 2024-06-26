%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cleanNLP
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Tidy Data Model for Natural Language Processing

License:          LGPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix >= 1.2
BuildRequires:    R-CRAN-udpipe 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-Matrix >= 1.2
Requires:         R-CRAN-udpipe 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-stringi 
Requires:         R-stats 
Requires:         R-methods 

%description
Provides a set of fast tools for converting a textual corpus into a set of
normalized tables. Users may make use of the 'udpipe' back end with no
external dependencies, or a Python back ends with 'spaCy'
<https://spacy.io>. Exposed annotation tasks include tokenization, part of
speech tagging, named entity recognition, and dependency parsing.

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
