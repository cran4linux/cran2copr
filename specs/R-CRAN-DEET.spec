%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DEET
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Differential Expression Enrichment Tool

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ActivePathways 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-downloader 
Requires:         R-CRAN-ActivePathways 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-downloader 

%description
RNA sequencing (RNA-seq) followed by differential gene expression analyses
is a fundamental approach for making biological discoveries. Ongoing
large-scale efforts to systematically process and normalize publicly
available gene expression data facilitate rapid reanalyses of specific
studies and the development of new methods for querying it. While there
are several powerful tools for querying systematically processed publicly
available RNA-seq data at the individual sample level, there are fewer
options for querying differentially expressed gene (DEG) lists generated
from these experiments. Here, we present the Differential Expression
Enrichment Tool (DEET), which allows users to interact with 3162
consistently processed DEG lists curated from 142 RNA-seq datasets
obtained from recount2 database, which contains data from consortiums
(GTex, TCGA) and individual labs (SRA). To establish DEET we integrated
systematically processed human RNA-seq data from recount2 with reported
and predicted metadata from multiple sources and developed a CRAN R
package and Shiny App where users can compare their genes, p-values, and
coefficients against the DEG lists within DEET. Here we present DEET and
demonstrate how it can facilitate hypothesis generation and provide
biological insight from user-defined differential gene expression results.
Reference: Sokolowski,D.J., Ahn J., Erdman,L., Hou,H., Ellis,K., Wang L.,
Goldenberg,A., and Wilson,M.D. (2022) Differential Expression Enrichment
Tool (DEET): An interactive atlas of human differential gene expression.
(In Preparation).

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
