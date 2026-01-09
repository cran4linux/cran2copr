%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MicrobiomeStat
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for Microbiome Compositional Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-modeest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mlrMBO 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ParamHelpers 
BuildRequires:    R-CRAN-smoof 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-mlr 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-matrixStats 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-modeest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mlrMBO 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ParamHelpers 
Requires:         R-CRAN-smoof 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-mlr 
Requires:         R-CRAN-BBmisc 

%description
A suite of methods for powerful and robust microbiome data analysis
addressing zero-inflation, phylogenetic structure and compositional
effects. Includes the LinDA method for differential abundance analysis
(Zhou et al. (2022)<doi:10.1186/s13059-022-02655-5>), the BMDD (Bimodal
Dirichlet Distribution) method for accurate modeling and imputation of
zero-inflated microbiome sequencing data (Zhou et al.
(2025)<doi:10.1371/journal.pcbi.1013124>) and compositional sparse CCA
methods for microbiome multi-omics data integration (Deng et al. (2024)
<doi: 10.3389/fgene.2024.1489694>).

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
