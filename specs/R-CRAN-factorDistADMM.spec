%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  factorDistADMM
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Distributed ADMM for High-Dimensional Static Factor Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-MASS 

%description
Distributed Alternating Direction Method of Multipliers (ADMM) algorithms
for high-dimensional static factor models. It provides a suite of
distributed statistical estimators, including centralized Principal
Component Analysis (PCA, C-PCA), distributed offline Principal Component
Analysis (D-PCA), distributed online Expectation-Maximization (EM, D-EM),
standard distributed Alternating Direction Method of Multipliers (S-ADMM),
and the proposed penalized distributed online Alternating Direction Method
of Multipliers (ADMM) with Lasso sparsity regularization. Trace-enabled
versions of all algorithms are implemented to record the Frobenius
estimation error and augmented Lagrangian values across iterations for
convergence diagnosis. This package is suitable for large-scale
high-dimensional data distributed over multiple computing nodes, where raw
data cannot be gathered onto a single machine. It offers flexible
simulation tools to generate static factor model data with sparse loadings
and weak temporal dependence. The methodology of 'factorDistADMM' is
described in Guo G. (2026) <doi:10.1016/j.jmva.2026.105688>.

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
