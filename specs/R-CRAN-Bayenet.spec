%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Bayenet
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Quantile Elastic Net for Genetic Study

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-base 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-hbmem 
BuildRequires:    R-CRAN-SuppDists 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-MCMCpack 
Requires:         R-base 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-hbmem 
Requires:         R-CRAN-SuppDists 

%description
As heavy-tailed error distribution and outliers in the response variable
widely exist, models which are robust to data contamination are highly
demanded. Here, we develop a novel robust Bayesian variable selection
method with elastic net penalty for quantile regression in genetic
analysis. In particular, the spike-and-slab priors have been incorporated
to impose sparsity. An efficient Gibbs sampler has been developed to
facilitate computation.The core modules of the package have been developed
in 'C++' and R.

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
