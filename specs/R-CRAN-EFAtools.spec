%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EFAtools
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast and Flexible Implementations of Exploratory Factor Analysis Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-roptim 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-psych 
Requires:         R-stats 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-lifecycle 

%description
Provides a complete workflow for exploratory factor analysis (EFA). It
covers data screening and factorability checks, a suite of factor
retention criteria for choosing the number of factors, and factor
extraction by principal axis factoring, maximum likelihood, unweighted
least squares, or diagonally weighted least squares from Pearson,
Spearman, Kendall, polychoric, tetrachoric, or two-stage full-information
maximum likelihood correlations. A built-in rotation engine offers a range
of orthogonal and oblique rotations, and standard errors for loadings and
related quantities can be obtained by analytic, robust, or bootstrap
methods. Further tools support model averaging across analytic choices,
multigroup EFA with factor congruence, EFA on multiply imputed data,
Schmid-Leiman transformation, reliability coefficients (including
McDonald's omegas), factor score estimation, data simulation, and power
analysis. Computationally intensive procedures are implemented in 'C++'
for speed.

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
