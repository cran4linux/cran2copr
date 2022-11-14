%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sentencepiece
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Text Tokenization using Byte Pair Encoding and Unigram Modelling

License:          MPL-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-stats 

%description
Unsupervised text tokenizer allowing to perform byte pair encoding and
unigram modelling. Wraps the 'sentencepiece' library
<https://github.com/google/sentencepiece> which provides a language
independent tokenizer to split text in words and smaller subword units.
The techniques are explained in the paper "SentencePiece: A simple and
language independent subword tokenizer and detokenizer for Neural Text
Processing" by Taku Kudo and John Richardson (2018)
<doi:10.18653/v1/D18-2012>. Provides as well straightforward access to
pretrained byte pair encoding models and subword embeddings trained on
Wikipedia using 'word2vec', as described in "BPEmb: Tokenization-free
Pre-trained Subword Embeddings in 275 Languages" by Benjamin Heinzerling
and Michael Strube (2018)
<http://www.lrec-conf.org/proceedings/lrec2018/pdf/1049.pdf>.

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
