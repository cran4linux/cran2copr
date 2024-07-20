%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  longevity
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for the Analysis of Excess Lifetimes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.6
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.6
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rsolnp 

%description
A collection of parametric and nonparametric methods for the analysis of
survival data. Parametric families implemented include Gompertz-Makeham,
exponential and generalized Pareto models and extended models. The package
includes an implementation of the nonparametric maximum likelihood
estimator for arbitrary truncation and censoring pattern based on Turnbull
(1976) <doi:10.1111/j.2517-6161.1976.tb01597.x>, along with graphical
goodness-of-fit diagnostics. Parametric models for positive random
variables and peaks over threshold models based on extreme value theory
are described in Rootzén and Zholud (2017)
<doi:10.1007/s10687-017-0305-5>; Belzile et al. (2021)
<doi:10.1098/rsos.202097> and Belzile et al. (2022)
<doi:10.1146/annurev-statistics-040120-025426>.

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
