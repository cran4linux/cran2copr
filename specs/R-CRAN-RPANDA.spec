%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RPANDA
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Phylogenetic ANalyses of DiversificAtion

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-mvMORPH >= 1.1.6
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-picante 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-bipartite 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-glassoFast 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-GUniFrac 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ParallelLogger 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-pspline 
BuildRequires:    R-CRAN-pvclust 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TESS 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-mvMORPH >= 1.1.6
Requires:         R-CRAN-ape 
Requires:         R-CRAN-picante 
Requires:         R-methods 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-bipartite 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-glassoFast 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-GUniFrac 
Requires:         R-parallel 
Requires:         R-CRAN-ParallelLogger 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-pspline 
Requires:         R-CRAN-pvclust 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-Rmpfr 
Requires:         R-stats 
Requires:         R-CRAN-TESS 
Requires:         R-utils 
Requires:         R-CRAN-vegan 

%description
Implements macroevolutionary analyses on phylogenetic trees. See Morlon et
al. (2010) <DOI:10.1371/journal.pbio.1000493>, Morlon et al. (2011)
<DOI:10.1073/pnas.1102543108>, Condamine et al. (2013)
<DOI:10.1111/ele.12062>, Morlon et al. (2014) <DOI:10.1111/ele.12251>,
Manceau et al. (2015) <DOI:10.1111/ele.12415>, Lewitus & Morlon (2016)
<DOI:10.1093/sysbio/syv116>, Drury et al. (2016)
<DOI:10.1093/sysbio/syw020>, Manceau et al. (2016)
<DOI:10.1093/sysbio/syw115>, Morlon et al. (2016)
<DOI:10.1111/2041-210X.12526>, Clavel & Morlon (2017)
<DOI:10.1073/pnas.1606868114>, Drury et al. (2017)
<DOI:10.1093/sysbio/syx079>, Lewitus & Morlon (2017)
<DOI:10.1093/sysbio/syx095>, Drury et al. (2018)
<DOI:10.1371/journal.pbio.2003563>, Clavel et al. (2019)
<DOI:10.1093/sysbio/syy045>, Maliet et al. (2019)
<DOI:10.1038/s41559-019-0908-0>, Billaud et al. (2019)
<DOI:10.1093/sysbio/syz057>, Lewitus et al. (2019)
<DOI:10.1093/sysbio/syz061>, Aristide & Morlon (2019)
<DOI:10.1111/ele.13385>, Maliet et al. (2020) <DOI:10.1111/ele.13592>,
Drury et al. (2021) <DOI:10.1371/journal.pbio.3001270>, Perez-Lamarque &
Morlon (2022) <DOI:10.1111/mec.16478>, Perez-Lamarque et al. (2022)
<DOI:10.1101/2021.08.30.458192>, Mazet et al. (2023)
<DOI:10.1111/2041-210X.14195>, Drury et al. (2024)
<DOI:10.1016/j.cub.2023.12.055>.

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
