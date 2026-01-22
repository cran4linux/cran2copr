%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plmmr
%global packver   4.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized Linear Mixed Models for Correlated Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildRequires:    R-CRAN-biglasso >= 1.6.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.8.600
BuildRequires:    R-CRAN-bigalgebra 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-biglasso >= 1.6.0
Requires:         R-CRAN-bigalgebra 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ncvreg 
Requires:         R-parallel 
Requires:         R-utils 

%description
Fits penalized linear mixed models that correct for unobserved confounding
factors. 'plmmr' infers and corrects for the presence of unobserved
confounding effects such as population stratification and environmental
heterogeneity. It then fits a linear model via penalized maximum
likelihood. Originally designed for the multivariate analysis of single
nucleotide polymorphisms (SNPs) measured in a genome-wide association
study (GWAS), 'plmmr' eliminates the need for subpopulation-specific
analyses and post-analysis p-value adjustments.  Functions for the
appropriate processing of 'PLINK' files are also supplied. For examples,
see the package homepage. <https://pbreheny.github.io/plmmr/>.

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
