%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastconley
%global packver   0.11.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Conley Standard Errors for 'lfe' and 'fixest' Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Conley (1999) <doi:10.1016/S0304-4076(98)00084-0> spatial
heteroscedasticity and autocorrelation consistent (HAC) standard errors
for fixed effects panel and cross-sectional models estimated with felm()
from the 'lfe' package (ordinary least squares and instrumental variables)
or with feols(), feglm(), and fepois() from the 'fixest' package.
Instrumental-variable support is limited to ordinary two-stage least
squares. Generalized linear model fits use the M-estimation sandwich built
from the stored scores and inverse Hessian. The spatial path uses score
accumulation, a three-dimensional cell-grid neighbour search, and
compressed sparse row neighbour lists instead of dense distance matrices,
yielding large speedups over the original 'conley' package
<https://github.com/rbluhm/conley> on big cross-sections and
high-dimensional regressions.

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
