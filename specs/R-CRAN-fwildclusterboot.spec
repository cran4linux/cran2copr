%global __brp_check_rpaths %{nil}
%global packname  fwildclusterboot
%global packver   0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Wild Cluster Bootstrap Inference for Linear Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-collapse 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-dreamerr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Matrix.utils 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-dqrng 
BuildRequires:    R-CRAN-JuliaConnectoR 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-dreamerr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Matrix.utils 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-dqrng 
Requires:         R-CRAN-JuliaConnectoR 

%description
Implementation of the fast algorithm for wild cluster bootstrap inference
developed in Roodman et al (2019, STATA Journal) for linear regression
models <doi:10.1177/1536867X19830877>, which makes it feasible to quickly
calculate bootstrap test statistics based on a large number of bootstrap
draws even for large samples. Multiway clustering, regression weights,
bootstrap weights, fixed effects and subcluster bootstrapping are
supported. Further, both restricted (WCR) and unrestricted (WCU) bootstrap
are supported. Methods are provided for a variety of fitted models,
including 'lm()', 'feols()' (from package 'fixest') and 'felm()' (from
package 'lfe'). Additionally implements a heteroskedasticity-robust (HC1)
wild bootstrap. Further, the package provides an R binding to
'WildBootTests.jl', which provides additional speed gains and
functionality, including the 'WRE' bootstrap for instrumental variable
models (based on models of type 'ivreg()' from package 'ivreg') and
hypotheses with q > 1.

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
