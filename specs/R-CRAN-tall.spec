%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tall
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Text Analysis for All

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-ca 
BuildRequires:    R-CRAN-chromote 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-fontawesome 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-pagedown 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readtext 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinydashboardPlus 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-sparkline 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-textrank 
BuildRequires:    R-CRAN-tidygraph 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-topicmodels 
BuildRequires:    R-CRAN-udpipe 
BuildRequires:    R-CRAN-umap 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-word2vec 
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-ca 
Requires:         R-CRAN-chromote 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-fontawesome 
Requires:         R-CRAN-ggraph 
Requires:         R-graphics 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-later 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-pagedown 
Requires:         R-parallel 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readtext 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinydashboardPlus 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-sparkline 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-textrank 
Requires:         R-CRAN-tidygraph 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-topicmodels 
Requires:         R-CRAN-udpipe 
Requires:         R-CRAN-umap 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-word2vec 

%description
An R 'shiny' app designed for diverse text analysis tasks, offering a wide
range of methodologies tailored to Natural Language Processing (NLP)
needs. It is a versatile, general-purpose tool for analyzing textual data.
'tall' features a comprehensive workflow, including data cleaning,
preprocessing, statistical analysis, and visualization, all integrated for
effective text analysis.

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
