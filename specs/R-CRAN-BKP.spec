%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BKP
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Beta Kernel Process Modeling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-dirmult 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-tgp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-dirmult 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-tgp 

%description
Implements the Beta Kernel Process (BKP) for nonparametric modeling of
covariate-dependent binomial probabilities, and the Dirichlet Kernel
Process (DKP) for categorical or multinomial response data. Scalable
global-local approximations are provided through TwinBKP and TwinDKP,
using twinning-selected global subsets and local nearest-neighbour
updates. Functions are included for model fitting, predictive inference
with uncertainty quantification, posterior simulation, and visualization
in one- and two-dimensional input spaces. Gaussian, Matern 5/2, Matern
3/2, and Wendland kernels are supported, with hyperparameters selected by
multi-start derivative-free optimization. For more details, see Zhao,
Qing, and Xu (2025) <doi:10.48550/arXiv.2508.10447>.

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
