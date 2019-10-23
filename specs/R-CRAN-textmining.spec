%global packname  textmining
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Integration of Text Mining and Topic Modeling Packages

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stylo 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-NLP 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-mallet 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-koRpus 
BuildRequires:    R-CRAN-topicmodels 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-SnowballC 
Requires:         R-CRAN-stylo 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-NLP 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-mallet 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-koRpus 
Requires:         R-CRAN-topicmodels 
Requires:         R-CRAN-slam 
Requires:         R-methods 
Requires:         R-CRAN-SnowballC 

%description
A framework for text mining and topic modelling. It provides an easy
interface for using different topic modeling methods within R, by
integrating the already existing packages. Full functionality of the
package requires a local installation of 'TreeTagger'.

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
