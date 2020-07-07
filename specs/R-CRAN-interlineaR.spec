%global packname  interlineaR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Importing Interlinearized Corpora and Dictionaries as Producedby Descriptive Linguistics Software

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-reshape2 

%description
Interlinearized glossed texts (IGT) are used in descriptive linguistics
for representing a morphological analysis of a text through a
morpheme-by-morpheme gloss. 'InterlineaR' provide a set of functions that
targets several popular formats of IGT ('SIL Toolbox', 'EMELD XML') and
that turns an IGT into a set of data frames following a relational model
(the tables represent the different linguistic units: texts, sentences,
word, morphems). The same pieces of software ('SIL FLEX', 'SIL Toolbox')
typically produce dictionaries of the morphemes used in the glosses.
'InterlineaR' provide a function for turning the LIFT XML dictionary
format into a set of data frames following a relational model in order to
represent the dictionary entries, the sense(s) attached to the entries,
the example(s) attached to senses, etc.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/exampleData
%{rlibdir}/%{packname}/INDEX
