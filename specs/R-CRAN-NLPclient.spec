%global packname  NLPclient
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Stanford 'CoreNLP' Annotation Client

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-NLP >= 0.1.10
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-NLP >= 0.1.10
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-curl 

%description
Stanford 'CoreNLP' annotation client. Stanford 'CoreNLP'
<https://stanfordnlp.github.io/CoreNLP/index.html> integrates all NLP
tools from the Stanford Natural Language Processing Group, including a
part-of-speech (POS) tagger, a named entity recognizer (NER), a parser,
and a coreference resolution system, and provides model files for the
analysis of English. More information can be found in the README.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
