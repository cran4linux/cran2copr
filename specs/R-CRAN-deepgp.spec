%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deepgp
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Deep Gaussian Processes using MCMC

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-GpGp 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-GpGp 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-abind 

%description
Performs Bayesian posterior inference for deep Gaussian processes
following Sauer, Gramacy, and Higdon (2023,
<doi:10.48550/arXiv.2012.08015>). See Sauer (2023,
<http://hdl.handle.net/10919/114845>) for comprehensive methodological
details and <https://bitbucket.org/gramacylab/deepgp-ex/> for a variety of
coding examples. Models are trained through MCMC including elliptical
slice sampling of latent Gaussian layers and Metropolis-Hastings sampling
of kernel hyperparameters.  Gradient-enhancement and gradient predictions
are offered following Booth (2025, <doi:10.48550/arXiv.2512.18066>).
Vecchia approximation for faster computation is implemented following
Sauer, Cooper, and Gramacy (2023, <doi:10.48550/arXiv.2204.02904>).
Optional monotonic warpings are implemented following Barnett et al.
(2025, <doi:10.48550/arXiv.2408.01540>). Downstream tasks include
sequential design through active learning Cohn/integrated mean squared
error (ALC/IMSE; Sauer, Gramacy, and Higdon, 2023), optimization through
expected improvement (EI; Gramacy, Sauer, and Wycoff, 2022,
<doi:10.48550/arXiv.2112.07457>), and contour location through entropy
(Booth, Renganathan, and Gramacy, 2025, <doi:10.48550/arXiv.2308.04420>).
Models extend up to three layers deep; a one layer model is equivalent to
typical Gaussian process regression. Incorporates OpenMP and SNOW
parallelization and utilizes C/C++ under the hood.

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
