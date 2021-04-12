%global packname  bayesImageS
%global packver   0.6-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Methods for Image Segmentation using a Potts Model

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.6
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.10.6

%description
Various algorithms for segmentation of 2D and 3D images, such as computed
tomography and satellite remote sensing. This package implements Bayesian
image analysis using the hidden Potts model with external field prior of
Moores et al. (2015) <doi:10.1016/j.csda.2014.12.001>. Latent labels are
sampled using chequerboard updating or Swendsen-Wang. Algorithms for the
smoothing parameter include pseudolikelihood, path sampling, the exchange
algorithm, approximate Bayesian computation (ABC-MCMC and ABC-SMC), and
the parametric functional approximate Bayesian (PFAB) algorithm. Refer to
<doi:10.1007/978-3-030-42553-1_6> for an overview and also to
<doi:10.1007/s11222-014-9525-6> and <doi:10.1214/18-BA1130> for further
details of specific algorithms.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
