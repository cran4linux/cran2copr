%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DEET
%global packver   1.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
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
Abstract of Manuscript. Differential gene expression analysis using RNA
sequencing (RNA-seq) data is a standard approach for making biological
discoveries. Ongoing large-scale efforts to process and normalize publicly
available gene expression data enable rapid and systematic reanalysis.
While several powerful tools systematically process RNA-seq data, enabling
their reanalysis, few resources systematically recompute differentially
expressed genes (DEGs) generated from individual studies. We developed a
robust differential expression analysis pipeline to recompute 3162 human
DEG lists from The Cancer Genome Atlas, Genotype-Tissue Expression
Consortium, and 142 studies within the Sequence Read Archive. After
measuring the accuracy of the recomputed DEG lists, we built the
Differential Expression Enrichment Tool (DEET), which enables users to
interact with the recomputed DEG lists. DEET, available through CRAN and
RShiny, systematically queries which of the recomputed DEG lists share
similar genes, pathways, and TF targets to their own gene lists. DEET
identifies relevant studies based on shared results with the user’s gene
lists, aiding in hypothesis generation and data-driven literature review.
Sokolowski, Dustin J., et al. "Differential Expression Enrichment Tool
(DEET): an interactive atlas of human differential gene expression."
Nucleic Acids Research Genomics and Bioinformatics (2023).

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
