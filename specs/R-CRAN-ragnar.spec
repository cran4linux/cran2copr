%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ragnar
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieval-Augmented Generation (RAG) Workflows

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-reticulate >= 1.42.0
BuildRequires:    R-CRAN-duckdb >= 1.3.1
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-blob 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-commonmark 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-reticulate >= 1.42.0
Requires:         R-CRAN-duckdb >= 1.3.1
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-blob 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-commonmark 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-httr2 
Requires:         R-methods 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-xml2 

%description
Provides tools for implementing Retrieval-Augmented Generation (RAG)
workflows with Large Language Models (LLM). Includes functions for
document processing, text chunking, embedding generation, storage
management, and content retrieval. Supports various document types and
embedding providers ('Ollama', 'OpenAI'), with 'DuckDB' as the default
storage backend. Integrates with the 'ellmer' package to equip chat
objects with retrieval capabilities. Designed to offer both sensible
defaults and customization options with transparent access to intermediate
outputs.  For a review of retrieval-augmented generation methods, see Gao
et al. (2023) "Retrieval-Augmented Generation for Large Language Models: A
Survey" <doi:10.48550/arXiv.2312.10997>.

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
