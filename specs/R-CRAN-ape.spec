%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ape
%global packver   5.7-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analyses of Phylogenetics and Evolution

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-lattice 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-digest 

%description
Functions for reading, writing, plotting, and manipulating phylogenetic
trees, analyses of comparative data in a phylogenetic framework, ancestral
character analyses, analyses of diversification and macroevolution,
computing distances from DNA sequences, reading and writing nucleotide
sequences as well as importing from BioConductor, and several tools such
as Mantel's test, generalized skyline plots, graphical exploration of
phylogenetic data (alex, trex, kronoviz), estimation of absolute
evolutionary rates and clock-like trees using mean path lengths and
penalized likelihood, dating trees with non-contemporaneous sequences,
translating DNA into AA sequences, and assessing sequence alignments.
Phylogeny estimation can be done with the NJ, BIONJ, ME, MVR, SDM, and
triangle methods, and several methods handling incomplete distance
matrices (NJ*, BIONJ*, MVR*, and the corresponding triangle method). Some
functions call external applications (PhyML, Clustal, T-Coffee, Muscle)
whose results are returned into R.

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
