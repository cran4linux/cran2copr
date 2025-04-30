%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RAGFlowChainR
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieval-Augmented Generation (RAG) Workflows in R with Local and Web Search

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-duckdb >= 0.10.0
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-duckdb >= 0.10.0
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-curl 

%description
Enables Retrieval-Augmented Generation (RAG) workflows in R by combining
local vector search using 'DuckDB' with optional web search via the
'Tavily' API. Supports OpenAI- and Ollama-compatible embedding models,
full-text and HNSW (Hierarchical Navigable Small World) indexing, and
modular large language model (LLM) invocation. Designed for advanced
question-answering, chat-based applications, and production-ready AI
pipelines. This package is the R equivalent of the 'python' package
'RAGFlowChain' available at <https://pypi.org/project/RAGFlowChain/>.

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
