%global packname  RPANDA
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          1%{?dist}
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
BuildRequires:    R-CRAN-pspline 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-TESS 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-pvclust 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-glassoFast 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-parallel 
Requires:         R-CRAN-mvMORPH >= 1.1.0
Requires:         R-CRAN-picante 
Requires:         R-methods 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-pspline 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-TESS 
Requires:         R-cluster 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-pvclust 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-phytools 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-mvtnorm 
Requires:         R-Matrix 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-glassoFast 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-coda 
Requires:         R-parallel 

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
<DOI:10.1093/sysbio/syz061>, and Aristide & Morlon (2019)
<DOI:10.1111/ele.13385>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
