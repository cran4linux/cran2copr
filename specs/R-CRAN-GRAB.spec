%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GRAB
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Genome-Wide Robust Analysis for Biobank Data (GRAB)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-ordinal 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-ordinal 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-igraph 

%description
Provides a comprehensive suite of genome-wide association study (GWAS)
methods specifically designed for biobank-scale data, including but not
limited to, robust approaches for time-to-event traits (Li et al., 2025
<doi:10.1038/s43588-025-00864-z>) and ordinal categorical traits (Bi et
al., 2021 <doi:10.1016/j.ajhg.2021.03.019>). The package also offers
general frameworks for GWAS of any trait type (Bi et al., 2020
<doi:10.1016/j.ajhg.2020.06.003>), while accounting for sample relatedness
(Xu et al., 2025 <doi:10.1038/s41467-025-56669-1>) or population structure
(Ma et al., 2025 <doi:10.1186/s13059-025-03827-9>). By accurately
approximating score statistic distributions using saddlepoint
approximation (SPA), these methods can effectively control type I error
rates for rare variants and in the presence of unbalanced phenotype
distributions. Additionally, the package includes functions for simulating
genotype and phenotype data to support research and method development.

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
