%global packname  hilldiv
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          2%{?dist}%{?buildtag}
Summary:          Integral Analysis of Diversity Based on Hill Numbers

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-FSA 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-FSA 

%description
Tools for analysing, comparing, visualising and partitioning diversity
based on Hill numbers. 'hilldiv' is an R package that provides a set of
functions to assist analysis of diversity for diet reconstruction,
microbial community profiling or more general ecosystem characterisation
analyses based on Hill numbers, using OTU/ASV tables and associated
phylogenetic trees as inputs. The package includes functions for
(phylo)diversity measurement, (phylo)diversity profile plotting,
(phylo)diversity comparison between samples and groups, (phylo)diversity
partitioning and (dis)similarity measurement. All of these grounded in
abundance-based and incidence-based Hill numbers. The statistical
framework developed around Hill numbers encompasses many of the most
broadly employed diversity (e.g. richness, Shannon index, Simpson index),
phylogenetic diversity (e.g. Faith's PD, Allen's H, Rao's quadratic
entropy) and dissimilarity (e.g. Sorensen index, Unifrac distances)
metrics. This enables the most common analyses of diversity to be
performed while grounded in a single statistical framework. The methods
are described in Jost et al. (2007) <DOI:10.1890/06-1736.1>, Chao et al.
(2010) <DOI:10.1098/rstb.2010.0272> and Chiu et al. (2014)
<DOI:10.1890/12-0960.1>; and reviewed in the framework of molecularly
characterised biological systems in Alberdi & Gilbert (2019)
<DOI:10.1111/1755-0998.13014>.

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

%files
%{rlibdir}/%{packname}
