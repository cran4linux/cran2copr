%global packname  cleanNLP
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          1%{?dist}
Summary:          A Tidy Data Model for Natural Language Processing

License:          LGPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         python2
Requires:         java
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-Matrix >= 1.2
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-Matrix >= 1.2
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-stringi 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 

%description
Provides a set of fast tools for converting a textual corpus into a set of
normalized tables. Users may make use of the 'udpipe' back end with no
external dependencies, a Python back end with 'spaCy' <https://spacy.io>
or the Java back end 'CoreNLP' <http://stanfordnlp.github.io/CoreNLP/>.
Exposed annotation tasks include tokenization, part of speech tagging,
named entity recognition, entity linking, sentiment analysis, dependency
parsing, coreference resolution, and word embeddings. Summary statistics
regarding token unigram, part of speech tag, and dependency type
frequencies are also included to assist with analyses.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/py
%doc %{rlibdir}/%{packname}/txt_files
%{rlibdir}/%{packname}/INDEX
