%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sommer
%global packver   4.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Solving Mixed Model Equations in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Matrix >= 1.1.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-Matrix >= 1.1.1
Requires:         R-CRAN-Rcpp >= 0.12.19
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-crayon 

%description
Structural multivariate-univariate linear mixed model solver for
estimation of multiple random effects with unknown variance-covariance
structures (e.g., heterogeneous and unstructured) and known covariance
among levels of random effects (e.g., pedigree and genomic relationship
matrices) (Covarrubias-Pazaran, 2016 <doi:10.1371/journal.pone.0156744>;
Maier et al., 2015 <doi:10.1016/j.ajhg.2014.12.006>; Jensen et al., 1997).
REML estimates can be obtained using the Direct-Inversion Newton-Raphson
and Direct-Inversion Average Information algorithms for the problems r x r
(r being the number of records) or using the Henderson-based average
information algorithm for the problem c x c (c being the number of
coefficients to estimate). Spatial models can also be fitted using the
two-dimensional spline functionality available.

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
