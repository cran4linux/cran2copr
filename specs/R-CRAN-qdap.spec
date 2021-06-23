%global __brp_check_rpaths %{nil}
%global packname  qdap
%global packver   2.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bridging the Gap Between Qualitative Data and Quantitative Analysis

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
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-NLP 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-venneuler 
BuildRequires:    R-CRAN-wordcloud 
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
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-NLP 
Requires:         R-CRAN-openxlsx 
Requires:         R-parallel 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-venneuler 
Requires:         R-CRAN-wordcloud 
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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
