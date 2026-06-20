%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  craftgrn
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Integrative Chromatin Accessibility and RNA Framework for Gene Regulatory Networks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-enrichR 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-LDAvis 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-config 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-enrichR 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-LDAvis 
Requires:         R-methods 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-yaml 

%description
Provides a reproducible framework for constructing and comparing gene
regulatory networks by integrating chromatin accessibility footprint
scores with matched RNA expression data. It implements context-specific
enhancer-gene linking, transcription factor focused network analysis,
differential network analysis, and regulatory topic modeling workflows for
systematic exploration of gene regulation across conditions.
Methodological background is described in Bentsen and others (2020)
<doi:10.1038/s41467-020-18035-1>, Blei, Ng and Jordan (2003)
<https://www.jmlr.org/papers/v3/blei03a.html>, and Chen, Li, Zhu and Chen
(2015) <doi:10.48550/arXiv.1510.08628>.

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
