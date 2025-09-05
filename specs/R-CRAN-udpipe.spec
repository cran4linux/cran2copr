%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  udpipe
%global packver   0.8.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.12
Release:          1%{?dist}%{?buildtag}
Summary:          Tokenization, Parts of Speech Tagging, Lemmatization and Dependency Parsing with the 'UDPipe' 'NLP' Toolkit

License:          MPL-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-stats 

%description
This natural language processing toolkit provides language-agnostic
'tokenization', 'parts of speech tagging', 'lemmatization' and 'dependency
parsing' of raw text. Next to text parsing, the package also allows you to
train annotation models based on data of 'treebanks' in 'CoNLL-U' format
as provided at <https://universaldependencies.org/format.html>. The
techniques are explained in detail in the paper: 'Tokenizing, POS Tagging,
Lemmatizing and Parsing UD 2.0 with UDPipe', available at
<doi:10.18653/v1/K17-3009>. The toolkit also contains functionalities for
commonly used data manipulations on texts which are enriched with the
output of the parser. Namely functionalities and algorithms for
collocations, token co-occurrence, document term matrix handling, term
frequency inverse document frequency calculations, information retrieval
metrics (Okapi BM25), handling of multi-word expressions, keyword
detection (Rapid Automatic Keyword Extraction, noun phrase extraction,
syntactical patterns) sentiment scoring and semantic similarity analysis.

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
