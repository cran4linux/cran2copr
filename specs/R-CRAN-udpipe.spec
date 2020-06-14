%global packname  udpipe
%global packver   0.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          2%{?dist}
Summary:          Tokenization, Parts of Speech Tagging, Lemmatization andDependency Parsing with the 'UDPipe' 'NLP' Toolkit

License:          MPL-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-Matrix 
Requires:         R-methods 

%description
This natural language processing toolkit provides language-agnostic
'tokenization', 'parts of speech tagging', 'lemmatization' and 'dependency
parsing' of raw text. Next to text parsing, the package also allows you to
train annotation models based on data of 'treebanks' in 'CoNLL-U' format
as provided at <http://universaldependencies.org/format.html>. The
techniques are explained in detail in the paper: 'Tokenizing, POS Tagging,
Lemmatizing and Parsing UD 2.0 with UDPipe', available at
<doi:10.18653/v1/K17-3009>.

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
%doc %{rlibdir}/%{packname}/conll17
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/dummydata
%doc %{rlibdir}/%{packname}/models-ud-2.0
%doc %{rlibdir}/%{packname}/models-ud-2.3
%doc %{rlibdir}/%{packname}/models-ud-2.4
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
