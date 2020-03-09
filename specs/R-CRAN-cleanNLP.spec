%global packname  cleanNLP
%global packver   3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.2
Release:          1%{?dist}
Summary:          A Tidy Data Model for Natural Language Processing

License:          LGPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         python2
Requires:         java
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-Matrix >= 1.2
BuildRequires:    R-CRAN-udpipe 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-Matrix >= 1.2
Requires:         R-CRAN-udpipe 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-stringi 
Requires:         R-stats 
Requires:         R-methods 

%description
Provides a set of fast tools for converting a textual corpus into a set of
normalized tables. Users may make use of the 'udpipe' back end with no
external dependencies, or two Python back ends with 'spaCy'
<https://spacy.io> or 'CoreNLP' <http://stanfordnlp.github.io/CoreNLP/>.
Exposed annotation tasks include tokenization, part of speech tagging,
named entity recognition, and dependency parsing.

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
%doc %{rlibdir}/%{packname}/txt_files
%{rlibdir}/%{packname}/INDEX
