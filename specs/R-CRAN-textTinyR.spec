%global packname  textTinyR
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Text Processing for Small or Big Data Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.8
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-Matrix 
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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/example_files
%doc %{rlibdir}/%{packname}/locale
%doc %{rlibdir}/%{packname}/stopwords
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
