%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PAGFL
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Joint Estimation of Latent Groups and Group-Specific Coefficients in Panel Data Models

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-RcppParallel 

%description
Latent group structures are a common challenge in panel data analysis.
Disregarding group-level heterogeneity can introduce bias. Conversely,
estimating individual coefficients for each cross-sectional unit is
inefficient and may lead to high uncertainty. This package addresses the
issue of unobservable group structures by implementing the pairwise
adaptive group fused Lasso (PAGFL) by Mehrabani (2023)
<doi:10.1016/j.jeconom.2022.12.002>. PAGFL identifies latent group
structures and group-specific coefficients in a single step. On top of
that, we extend the PAGFL to time-varying coefficient functions.

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
