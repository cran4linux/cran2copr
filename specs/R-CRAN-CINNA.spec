%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CINNA
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Deciphering Central Informative Nodes in Network Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-centiserve 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-intergraph 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-network 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-centiserve 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-intergraph 
Requires:         R-utils 
Requires:         R-stats 

%description
Computing, comparing, and demonstrating top informative centrality
measures within a network. "CINNA: an R/CRAN package to decipher Central
Informative Nodes in Network Analysis" provides a comprehensive overview
of the package functionality Ashtiani et al. (2018)
<doi:10.1093/bioinformatics/bty819>.

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
