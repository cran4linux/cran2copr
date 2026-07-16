%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nmathopencl
%global packver   0.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          1%{?dist}%{?buildtag}
Summary:          'OpenCL'-Ported R 'Mathlib' for GPU-Accelerated Packages

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.1.1
BuildRequires:    R-CRAN-opencltools >= 0.8.2
BuildRequires:    R-CRAN-Rdpack >= 0.11.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.1.1
Requires:         R-CRAN-opencltools >= 0.8.2
Requires:         R-CRAN-Rdpack >= 0.11.0
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-RcppParallel 

%description
Ships statistical and mathematical routines from R internal 'nmath'
('Mathlib') as 'OpenCL' C sources under directory 'inst/cl/', with R
wrappers that use the GPU when 'OpenCL' is available at compile time and
fall back to 'stats' equivalents otherwise. Aimed at package developers
building custom kernels (for example Bayesian GLMs via suggested package
'glmbayes') using 'opencltools' kernel loaders and related helpers.
Contains translated shims, an illustrative GLM-related kernel subsystem,
vignettes, and optional GPU acceleration. The ported routines are
translated from the 'nmath' ('Mathlib') and 'Rmath' sources of R Core Team
(2026) "R: A Language and Environment for Statistical Computing"
<doi:10.32614/R.manuals>. 'OpenCL' GPU execution follows the standard
described in Stone, Gohara, and Shi (2010) <doi:10.1109/MCSE.2010.69>. The
likelihood subgradient simulation methodology implemented by the
illustrative GLM kernel subsystem is described in Nygren and Nygren (2006)
<doi:10.1198/016214506000000357>.

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
