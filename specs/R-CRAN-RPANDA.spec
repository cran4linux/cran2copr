%global packname  RPANDA
%global packver   1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Phylogenetic ANalyses of DiversificAtion

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.2
Requires:         R-core >= 2.14.2
BuildRequires:    R-CRAN-mvMORPH >= 1.1.0
BuildRequires:    R-CRAN-picante 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-bipartite 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-glassoFast 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-pspline 
BuildRequires:    R-CRAN-pvclust 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TESS 
BuildRequires:    R-utils 
Requires:         R-CRAN-mvMORPH >= 1.1.0
Requires:         R-CRAN-picante 
Requires:         R-methods 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-bipartite 
Requires:         R-cluster 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-glassoFast 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-igraph 
Requires:         R-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-pspline 
Requires:         R-CRAN-pvclust 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-Rmpfr 
Requires:         R-stats 
Requires:         R-CRAN-TESS 
Requires:         R-utils 

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
<DOI:10.1111/ele.13385>, and Maliet et al. (2020) <DOI:10.1111/ele.13592>.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
