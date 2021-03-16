%global packname  quanteda.textstats
%global packver   0.93
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.93
Release:          1%{?dist}%{?buildtag}
Summary:          Textual Statistics for the Quantitative Analysis of Textual Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.600.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-proxyC >= 0.1.4
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nsyllable 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-proxyC >= 0.1.4
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-nsyllable 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-stringi 

%description
Textual statistics functions formerly in the 'quanteda' package. Textual
statistics for characterizing and comparing textual data. Includes
functions for measuring term and document frequency, the co-occurrence of
words, similarity and distance between features and documents, feature
entropy, keyword occurrence, readability, and lexical diversity.  These
functions extend the 'quanteda' package and are specially designed for
sparse textual data.

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
