%global packname  revtools
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Tools to Support Evidence Synthesis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-modeltools 
BuildRequires:    R-CRAN-NLP 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-topicmodels 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-modeltools 
Requires:         R-CRAN-NLP 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-topicmodels 
Requires:         R-CRAN-viridisLite 

%description
Researchers commonly need to summarize scientific information, a process
known as 'evidence synthesis'. The first stage of a synthesis process
(such as a systematic review or meta-analysis) is to download a list of
references from academic search engines such as 'Web of Knowledge' or
'Scopus'. The traditional approach to systematic review is then to sort
these data manually, first by locating and removing duplicated entries,
and then screening to remove irrelevant content by viewing titles and
abstracts (in that order). 'revtools' provides interfaces for each of
these tasks. An alternative approach, however, is to draw on tools from
machine learning to visualise patterns in the corpus. In this case, you
can use 'revtools' to render ordinations of text drawn from article
titles, keywords and abstracts, and interactively select or exclude
individual references, words or topics.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
