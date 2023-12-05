%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  textTinyR
%global packver   1.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Text Processing for Small or Big Data Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.8
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-data.table 
Requires:         R-utils 

%description
It offers functions for splitting, parsing, tokenizing and creating a
vocabulary for big text data files. Moreover, it includes functions for
building a document-term matrix and extracting information from those
(term-associations, most frequent terms). It also embodies functions for
calculating token statistics (collocations, look-up tables, string
dissimilarities) and functions to work with sparse matrices. Lastly, it
includes functions for Word Vector Representations (i.e. 'GloVe',
'fasttext') and incorporates functions for the calculation of (pairwise)
text document dissimilarities. The source code is based on 'C++11' and
exported in R through the 'Rcpp', 'RcppArmadillo' and 'BH' packages.

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
