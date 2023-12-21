%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ontophylo
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Ontology-Informed Phylogenetic Comparative Analyses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-ontologyIndex 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-fANCOVA 
BuildRequires:    R-CRAN-grImport 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-ontologyIndex 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-grid 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-fANCOVA 
Requires:         R-CRAN-grImport 

%description
Provides new tools for analyzing discrete trait data integrating
bio-ontologies and phylogenetics. It expands on the previous work of
Tarasov et al. (2019) <doi:10.1093/isd/ixz009>. The PARAMO pipeline allows
to reconstruct ancestral phenomes treating groups of morphological traits
as a single complex character. The pipeline incorporates knowledge from
ontologies during the amalgamation of individual character stochastic
maps. Here we expand the current PARAMO functionality by adding new
statistical methods for inferring evolutionary phenome dynamics using
non-homogeneous Poisson process (NHPP). The new functionalities include:
(1) reconstruction of evolutionary rate shifts of phenomes across lineages
and time; (2) reconstruction of morphospace dynamics through time; and (3)
estimation of rates of phenome evolution at different levels of anatomical
hierarchy (e.g., entire body or specific regions only). The package also
includes user-friendly tools for visualizing evolutionary rates of
different anatomical regions using vector images of the organisms of
interest.

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
