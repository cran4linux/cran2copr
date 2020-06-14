%global packname  wordnet
%global packver   0.1-14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.14
Release:          2%{?dist}
Summary:          WordNet Interface

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
Requires:         wordnet
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava >= 0.6.3
Requires:         R-CRAN-rJava >= 0.6.3

%description
An interface to WordNet using the Jawbone Java API to WordNet. WordNet
(<http://wordnet.princeton.edu/>) is a large lexical database of English.
Nouns, verbs, adjectives and adverbs are grouped into sets of cognitive
synonyms (synsets), each expressing a distinct concept.  Synsets are
interlinked by means of conceptual-semantic and lexical relations. Please
note that WordNet(R) is a registered tradename.  Princeton University
makes WordNet available to research and commercial users free of charge
provided the terms of their license
(<http://wordnet.princeton.edu/wordnet/license/>) are followed, and proper
reference is made to the project using an appropriate citation
(<http://wordnet.princeton.edu/wordnet/citing-wordnet/>).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
