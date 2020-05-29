%global packname  hsrecombi
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
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
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-hsphase 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-quadprog 

%description
Paternal recombination rate and maternal linkage disequilibrium (LD) are
estimated for pairs of biallelic markers such as single nucleotide
polymorphisms (SNPs) from progeny genotypes and sire haplotypes. At least
one sire has to be double heterozygous at the investigated pairs of SNPs.
The implementation relies on paternal half-sib families. If maternal half-
sib families are used, the roles of sire/dam are swapped. Multiple
families can be considered. Hampel, Teuscher, Gomez-Raya, Doschoris,
Wittenburg (2018) "Estimation of recombination rate and maternal linkage
disequilibrium in half-sibs" <doi:10.3389/fgene.2018.00186>. Gomez-Raya
(2012) "Maximum likelihood estimation of linkage disequilibrium in
half-sib families" <doi:10.1534/genetics.111.137521>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
