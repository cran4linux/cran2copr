%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qfratio
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Moments and Distributions of Ratios of Quadratic Forms Using Recursion

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-MASS 
Requires:         R-stats 

%description
Evaluates moments of ratios (and products) of quadratic forms in normal
variables, specifically using recursive algorithms developed by Bao and
Kan (2013) <doi:10.1016/j.jmva.2013.03.002> and Hillier et al. (2014)
<doi:10.1017/S0266466613000364>. Also provides distribution, quantile, and
probability density functions of simple ratios of quadratic forms in
normal variables with several algorithms. Originally developed as a
supplement to Watanabe (2023) <doi:10.1007/s00285-023-01930-8> for
evaluating average evolvability measures in evolutionary quantitative
genetics, but can be used for a broader class of statistics. Generating
functions for these moments are also closely related to the top-order
zonal and invariant polynomials of matrix arguments.

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
