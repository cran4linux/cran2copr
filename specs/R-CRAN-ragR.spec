%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ragR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieval-Augmented Generation and RAG Evaluation Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-readtext 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-readtext 
Requires:         R-CRAN-tibble 

%description
Provides tools for document ingestion, embedding storage,
retrieval-augmented generation (RAG), and evaluation of question-answering
systems. The package includes an R-native vector store, wrappers for
OpenAI embedding and chat-completion application programming interfaces
(APIs), question-answering logging utilities, and large language model
(LLM)-based evaluation metrics for context precision, context recall,
answer relevance, and faithfulness. These metrics are based on the
Retrieval-Augmented Generation Assessment (RAGAS) framework. The
retrieval-augmented generation methodology is described by Lewis et al.
(2020) "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
<doi:10.48550/arXiv.2005.11401>. The evaluation metrics are based on Es et
al. (2024) "RAGAS: Automated Evaluation of Retrieval Augmented Generation"
<doi:10.18653/v1/2024.eacl-demo.16>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
