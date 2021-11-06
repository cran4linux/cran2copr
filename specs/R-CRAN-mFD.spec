%global __brp_check_rpaths %{nil}
%global packname  mFD
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compute and Illustrate the Multiple Facets of Functional Diversity

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-betapart >= 1.5.4
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-gawdis 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rstatix 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-betapart >= 1.5.4
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-gawdis 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-grid 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rstatix 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-vegan 

%description
Computing functional traits-based distances between pairs of species for
species gathered in assemblages allowing to build several functional
spaces. The package allows to compute functional diversity indices
assessing the distribution of species (and of their dominance) in a given
functional space for each assemblage and the overlap between assemblages
in a given functional space, see: Chao et al. (2018)
<doi:10.1002/ecm.1343>, Maire et al. (2015) <doi:10.1111/geb.12299>,
Mouillot et al. (2013) <doi:10.1016/j.tree.2012.10.004>, Mouillot et al.
(2014) <doi:10.1073/pnas.1317625111>, Ricotta and Szeidl (2009)
<doi:10.1016/j.tpb.2009.10.001>. Graphical outputs are included. Visit the
'mFD' website for more information, documentation and examples.

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
