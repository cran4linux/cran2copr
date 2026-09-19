%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MDgof
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Various Methods for the Goodness-of-Fit Problem in D>1 Dimensions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-MD2sample >= 1.4.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-microbenchmark 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-MD2sample >= 1.4.0
Requires:         R-CRAN-Rcpp 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-microbenchmark 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 

%description
Provides multivariate goodness-of-fit testing with a common interface for
several test statistics. Null models may be simple or include parameter
estimation, with p-values obtained by parametric bootstrap simulation. The
function gof_test_adjusted_pvalue() combines several tests and computes a
p-value adjusted for simultaneous inference. The function gof_power()
estimates test power. The functions hybrid_test() and hybrid_power() use
Monte Carlo samples under the null together with two-sample procedures.
The function run.studies() supports systematic power comparisons of
user-supplied and included methods across case studies. See the included
vignettes for method details and references.

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
