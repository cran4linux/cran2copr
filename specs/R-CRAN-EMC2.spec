%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EMC2
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Hierarchical Analysis of Cognitive Models of Choice

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Brobdingnag 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-WienR 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-corpcor 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-matrixcalc 
Requires:         R-methods 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Brobdingnag 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-psych 
Requires:         R-utils 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-WienR 

%description
Fit Bayesian (hierarchical) cognitive models using a linear modeling
language interface using particle Metropolis Markov chain Monte Carlo
sampling with Gibbs steps. The diffusion decision model (DDM), linear
ballistic accumulator model (LBA), racing diffusion model (RDM), and the
lognormal race model (LNR) are supported. Additionally, users can specify
their own likelihood function and/or choose for non-hierarchical
estimation, as well as for a diagonal, blocked or full multivariate normal
group-level distribution to test individual differences. Prior
specification is facilitated through methods that visualize the (implied)
prior. A wide range of plotting functions assist in assessing model
convergence and posterior inference. Models can be easily evaluated using
functions that plot posterior predictions or using relative model
comparison metrics such as information criteria or Bayes factors.
References: Stevenson et al. (2024) <doi:10.31234/osf.io/2e4dq>.

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
