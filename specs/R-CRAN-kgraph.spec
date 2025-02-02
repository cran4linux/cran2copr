%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kgraph
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Knowledge Graphs Constructions and Visualizations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-amap 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rsvd 
BuildRequires:    R-CRAN-sgraph 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-text2vec 
Requires:         R-CRAN-amap 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-grid 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rsvd 
Requires:         R-CRAN-sgraph 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-text2vec 

%description
Knowledge graphs enable to efficiently visualize and gain insights into
large-scale data analysis results, as p-values from multiple studies or
embedding data matrices. The usual workflow is a user providing a data
frame of association studies results and specifying target nodes, e.g.
phenotypes, to visualize. The knowledge graph then shows all the features
which are significantly associated with the phenotype, with the edges
being proportional to the association scores. As the user adds several
target nodes and grouping information about the nodes such as biological
pathways, the construction of such graphs soon becomes complex. The
'kgraph' package aims to enable users to easily build such knowledge
graphs, and provides two main features: first, to enable building a
knowledge graph based on a data frame of concepts relationships, be it
p-values or cosine similarities; second, to enable determining an
appropriate cut-off on cosine similarities from a complete embedding
matrix, to enable the building of a knowledge graph directly from an
embedding matrix. The 'kgraph' package provides several display, layout
and cut-off options, and has already proven useful to researchers to
enable them to visualize large sets of p-value associations with various
phenotypes, and to quickly be able to visualize embedding results. Two
example datasets are provided to demonstrate these behaviors, and several
live 'shiny' applications are hosted by the CELEHS laboratory and Parse
Health, as the KESER Mental Health application
<https://keser-mental-health.parse-health.org/> based on Hong C. (2021)
<doi:10.1038/s41746-021-00519-z>.

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
