%global packname  tokenizers
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Fast, Consistent Tokenization of Natural Language Text

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildRequires:    R-CRAN-stringi >= 1.0.1
BuildRequires:    R-CRAN-SnowballC >= 0.5.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-stringi >= 1.0.1
Requires:         R-CRAN-SnowballC >= 0.5.1
Requires:         R-CRAN-Rcpp >= 0.12.3

%description
Convert natural language text into tokens. Includes tokenizers for
shingled n-grams, skip n-grams, words, word stems, sentences, paragraphs,
characters, shingled characters, lines, tweets, Penn Treebank, regular
expressions, as well as functions for counting characters, words, and
sentences, and a function for splitting longer texts into separate
documents, each with the same number of words.  The tokenizers have a
consistent interface, and the package is built on the 'stringi' and 'Rcpp'
packages for fast yet correct tokenization in 'UTF-8'.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
