%global __brp_check_rpaths %{nil}
%global packname  RAINBOWR
%global packver   0.1.29
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.29
Release:          1%{?dist}%{?buildtag}
Summary:          Genome-Wide Association Study with SNP-Set Methods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-pegas 
BuildRequires:    R-CRAN-rrBLUP 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-gaston 
BuildRequires:    R-CRAN-MM4LMM 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pbmcapply 
Requires:         R-CRAN-optimx 
Requires:         R-methods 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-pegas 
Requires:         R-CRAN-rrBLUP 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-here 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-gaston 
Requires:         R-CRAN-MM4LMM 

%description
By using 'RAINBOWR' (Reliable Association INference By Optimizing Weights
with R), users can test multiple SNPs (Single Nucleotide Polymorphisms)
simultaneously by kernel-based (SNP-set) methods. This package can also be
applied to haplotype-based GWAS (Genome-Wide Association Study). Users can
test not only additive effects but also dominance and epistatic effects.
In detail, please check our paper on PLOS Computational Biology: Kosuke
Hamazaki and Hiroyoshi Iwata (2020) <doi:10.1371/journal.pcbi.1007663>.

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
