%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hsrecombi
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Recombination Rate and Maternal LD in Half-Sibs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-hsphase 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-hsphase 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-Matrix 

%description
Paternal recombination rate and maternal linkage disequilibrium (LD) are
estimated for pairs of biallelic markers such as single nucleotide
polymorphisms (SNPs) from progeny genotypes and sire haplotypes. The
implementation relies on paternal half-sib families. If maternal half-sib
families are used, the roles of sire/dam are swapped. Multiple families
can be considered. For parameter estimation, at least one sire has to be
double heterozygous at the investigated pairs of SNPs. Based on
recombination rates, genetic distances between markers can be estimated.
Markers with unusually large recombination rate to markers in close
proximity (i.e. putatively misplaced markers) shall be discarded in this
derivation. A workflow description is attached as vignette. *A pipeline is
available at GitHub* <https://github.com/wittenburg/hsrecombi> Hampel,
Teuscher, Gomez-Raya, Doschoris, Wittenburg (2018) "Estimation of
recombination rate and maternal linkage disequilibrium in half-sibs"
<doi:10.3389/fgene.2018.00186>. Gomez-Raya (2012) "Maximum likelihood
estimation of linkage disequilibrium in half-sib families"
<doi:10.1534/genetics.111.137521>.

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
