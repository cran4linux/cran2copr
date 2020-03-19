%global packname  quanteda
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Quantitative Analysis of Textual Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-Matrix >= 1.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.600.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-proxyC >= 0.1.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-extrafont 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-stopwords 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-Matrix >= 1.2
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-proxyC >= 0.1.4
Requires:         R-methods 
Requires:         R-CRAN-extrafont 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-network 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-stopwords 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-yaml 

%description
A fast, flexible, and comprehensive framework for quantitative text
analysis in R.  Provides functionality for corpus management, creating and
manipulating tokens and ngrams, exploring keywords in context, forming and
manipulating sparse matrices of documents by features and feature
co-occurrences, analyzing keywords, computing feature similarities and
distances, applying content dictionaries, applying supervised and
unsupervised machine learning, visually representing text and text
analyses, and more.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
