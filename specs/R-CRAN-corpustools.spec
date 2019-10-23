%global packname  corpustools
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}
Summary:          Managing, Querying and Analyzing Tokenized Text

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-wordcloud >= 2.5
BuildRequires:    R-Matrix >= 1.2
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-udpipe 
Requires:         R-CRAN-wordcloud >= 2.5
Requires:         R-Matrix >= 1.2
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-memoise 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-udpipe 

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
