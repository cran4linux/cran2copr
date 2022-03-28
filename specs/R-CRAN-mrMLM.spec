%global __brp_check_rpaths %{nil}
%global packname  mrMLM
%global packver   5.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Locus Random-SNP-Effect Mixed Linear Model Tools for GWAS

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-coin >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-sbl 
BuildRequires:    R-CRAN-BEDMatrix 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-coin >= 1.1.0
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-CRAN-lars 
Requires:         R-methods 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-sampling 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-sbl 
Requires:         R-CRAN-BEDMatrix 

%description
Conduct multi-locus genome-wide association study under the framework of
multi-locus random-SNP-effect mixed linear model (mrMLM). First, each
marker on the genome is scanned. Bonferroni correction is replaced by a
less stringent selection criterion for significant test. Then, all the
markers that are potentially associated with the trait are included in a
multi-locus genetic model, their effects are estimated by empirical Bayes,
and all the nonzero effects were further identified by likelihood ratio
test for significant QTL. The program may run on a desktop or laptop
computers. If marker genotypes in association mapping population are
almost homozygous, these methods in this software are very effective. If
there are many heterozygous marker genotypes, the IIIVmrMLM software is
recommended. Wen YJ, Zhang H, Ni YL, Huang B, Zhang J, Feng JY, Wang SB,
Dunwell JM, Zhang YM, Wu R (2018, <doi:10.1093/bib/bbw145>), and Li M,
Zhang YW, Zhang ZC, Xiang Y, Liu MH, Zhou YH, Zuo JF, Zhang HQ, Chen Y,
Zhang YM (2022, <doi:10.1016/j.molp.2022.02.012>).

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
