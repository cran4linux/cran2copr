%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  topolow
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Antigenic Mapping and Antigenic Velocity Algorithm

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.10.0
BuildRequires:    R-parallel >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-Racmacs >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rgl >= 1.0.0
BuildRequires:    R-CRAN-coda >= 0.19.4
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-filelock 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-umap 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-plotly >= 4.10.0
Requires:         R-parallel >= 4.1.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-Racmacs >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rgl >= 1.0.0
Requires:         R-CRAN-coda >= 0.19.4
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-filelock 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-umap 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ape 

%description
An implementation of the TopoLow algorithm, a novel, physics-inspired
method for antigenic cartography. TopoLow addresses significant challenges
in mapping antigenic relationships, especially from sparse and noisy
experimental data. The package transforms cross-reactivity and binding
affinity measurements into accurate spatial representations in a phenotype
space. Key features include: * Robust Mapping from Sparse Data:
Effectively creates complete and consistent maps even with high
proportions of missing data (e.g., >95%%). * Physics-Inspired Optimization:
Models antigens as particles connected by springs (for measured
interactions) and subject to repulsive forces (for missing interactions),
reducing the need for complex gradient computations. * Automatic
Dimensionality Detection: Employs a likelihood-based approach to determine
the optimal number of dimensions for the antigenic map, avoiding
distortions common in methods with fixed low dimensions. * Noise and Bias
Reduction: Naturally mitigates experimental noise and bias through its
network-based, error-dampening mechanism. * Antigenic Velocity
Calculation: Introduces and quantifies "antigenic velocity," a vector that
describes the rate and direction of antigenic drift for each pathogen
isolate. This can help identify cluster transitions and potential lineage
replacements. * Broad Applicability: Analyzes data from various pathogens,
including influenza, HIV, and Dengue viruses. It can be applied to any
continuous and relational phenotype under directional selection pressure.
Methods are described in Arhami and Rohani (2025)
<doi:10.1093/bioinformatics/btaf372>.

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
