%global packname  qdap
%global packver   2.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.2
Release:          1%{?dist}
Summary:          Bridging the Gap Between Qualitative Data and QuantitativeAnalysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-qdapTools >= 1.3.1
BuildRequires:    R-CRAN-qdapDictionaries >= 1.0.2
BuildRequires:    R-CRAN-tm >= 0.7.6
BuildRequires:    R-CRAN-gender >= 0.5.1
BuildRequires:    R-CRAN-dplyr >= 0.3
BuildRequires:    R-CRAN-openNLP >= 0.2.1
BuildRequires:    R-CRAN-qdapRegex >= 0.1.2
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-NLP 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-reports 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-venneuler 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-qdapTools >= 1.3.1
Requires:         R-CRAN-qdapDictionaries >= 1.0.2
Requires:         R-CRAN-tm >= 0.7.6
Requires:         R-CRAN-gender >= 0.5.1
Requires:         R-CRAN-dplyr >= 0.3
Requires:         R-CRAN-openNLP >= 0.2.1
Requires:         R-CRAN-qdapRegex >= 0.1.2
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-gdata 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-NLP 
Requires:         R-parallel 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-reports 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-CRAN-venneuler 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-XML 

%description
Automates many of the tasks associated with quantitative discourse
analysis of transcripts containing discourse including frequency counts of
sentence types, words, sentences, turns of talk, syllables and other
assorted analysis tasks. The package provides parsing tools for preparing
transcript data. Many functions enable the user to aggregate data by any
number of grouping variables, providing analysis and seamless integration
with other R packages that undertake higher level analysis and
visualization of text. This affords the user a more efficient and targeted
analysis. 'qdap' is designed for transcript analysis, however, many
functions are applicable to other areas of Text Mining/ Natural Language
Processing.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/Rmd_vignette
%{rlibdir}/%{packname}/INDEX
