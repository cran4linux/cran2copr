%global packname  corpustools
%global packver   0.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          1%{?dist}%{?buildtag}
Summary:          Managing, Querying and Analyzing Tokenized Text

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-wordcloud >= 2.5
BuildRequires:    R-CRAN-quanteda >= 1.5.1
BuildRequires:    R-CRAN-pbapply >= 1.4
BuildRequires:    R-CRAN-RNewsflow >= 1.2.1
BuildRequires:    R-CRAN-Matrix >= 1.2
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-udpipe >= 0.8.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-tokenbrowser >= 0.1.5
BuildRequires:    R-CRAN-rsyntax >= 0.1.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-wordcloud >= 2.5
Requires:         R-CRAN-quanteda >= 1.5.1
Requires:         R-CRAN-pbapply >= 1.4
Requires:         R-CRAN-RNewsflow >= 1.2.1
Requires:         R-CRAN-Matrix >= 1.2
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-udpipe >= 0.8.3
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-tokenbrowser >= 0.1.5
Requires:         R-CRAN-rsyntax >= 0.1.1
Requires:         R-methods 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-igraph 
Requires:         R-parallel 

%description
Provides text analysis in R, focusing on the use of a tokenized text
format. In this format, the positions of tokens are maintained, and each
token can be annotated (e.g., part-of-speech tags, dependency relations).
Prominent features include advanced Lucene-like querying for specific
tokens or contexts (e.g., documents, sentences), similarity statistics for
words and documents, exporting to DTM for compatibility with many text
analysis packages, and the possibility to reconstruct original text from
tokens to facilitate interpretation.

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
