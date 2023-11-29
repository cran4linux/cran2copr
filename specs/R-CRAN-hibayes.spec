%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hibayes
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Individual-Level, Summary-Level and Single-Step Bayesian Regression Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.600.0.0
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-CMplot 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-Matrix 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-CMplot 

%description
A user-friendly tool to fit Bayesian regression models. It can fit 3 types
of Bayesian models using individual-level, summary-level, and individual
plus pedigree-level (single-step) data for both Genomic
prediction/selection (GS) and Genome-Wide Association Study (GWAS), it was
designed to estimate joint effects and genetic parameters for a complex
trait, including: (1) fixed effects and coefficients of covariates, (2)
environmental random effects, and its corresponding variance, (3) genetic
variance, (4) residual variance, (5) heritability, (6) genomic estimated
breeding values (GEBV) for both genotyped and non-genotyped individuals,
(7) SNP effect size, (8) phenotype/genetic variance explained (PVE) for
single or multiple SNPs, (9) posterior probability of association of the
genomic window (WPPA), (10) posterior inclusive probability (PIP). The
functions are not limited, we will keep on going in enriching it with more
features. References: Meuwissen et al. (2001)
<doi:10.1093/genetics/157.4.1819>; Gustavo et al. (2013)
<doi:10.1534/genetics.112.143313>; Habier et al. (2011)
<doi:10.1186/1471-2105-12-186>; Yi et al. (2008)
<doi:10.1534/genetics.107.085589>; Zhou et al. (2013)
<doi:10.1371/journal.pgen.1003264>; Moser et al. (2015)
<doi:10.1371/journal.pgen.1004969>; Lloyd-Jones et al. (2019)
<doi:10.1038/s41467-019-12653-0>; Henderson (1976) <doi:10.2307/2529339>;
Fernando et al. (2014) <doi:10.1186/1297-9686-46-50>.

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
