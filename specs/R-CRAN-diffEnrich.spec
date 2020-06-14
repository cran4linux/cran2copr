%global packname  diffEnrich
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Given a List of Gene Symbols, Performs Differential EnrichmentAnalysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggnewscale 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-here 
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggnewscale 

%description
Compare functional enrichment between two experimentally-derived groups of
genes or proteins (Peterson, DR., et al.(2018)) <doi:
10.1371/journal.pone.0198139>. Given a list of gene symbols, 'diffEnrich'
will perform differential enrichment analysis using the Kyoto Encyclopedia
of Genes and Genomes (KEGG) REST API. This package provides a number of
functions that are intended to be used in a pipeline. Briefly, the user
provides a KEGG formatted species id for either human, mouse or rat, and
the package will download and clean species specific ENTREZ gene IDs and
map them to their respective KEGG pathways by accessing KEGG's REST API.
KEGG's API is used to guarantee the most up-to-date pathway data from
KEGG. Next, the user will identify significantly enriched pathways from
two gene sets, and finally, the user will identify pathways that are
differentially enriched between the two gene sets. In addition to the
analysis pipeline, this package also provides a plotting function.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
