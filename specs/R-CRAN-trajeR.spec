%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  trajeR
%global packver   0.11.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.1
Release:          1%{?dist}%{?buildtag}
Summary:          Group Based Modeling Trajectory

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.4.6
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-capushe 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.4.6
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-capushe 
Requires:         R-stats 

%description
Estimation of group-based trajectory models, including finite mixture
models for longitudinal data, supporting censored normal, zero-inflated
Poisson, logit, and beta distributions, using expectation-maximization and
quasi-Newton methods, with tools for model selection, diagnostics, and
visualization of latent trajectory groups, <doi:10.4159/9780674041318>,
Nagin, D. (2005). Group-Based Modeling of Development. Cambridge, MA:
Harvard University Press. and Noel (2022), <https://orbilu.uni.lu/>,
thesis.

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
