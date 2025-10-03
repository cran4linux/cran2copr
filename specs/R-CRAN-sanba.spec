%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sanba
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Shared Atoms Nested Models via MCMC or Variational Bayes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-salso 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-salso 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-RColorBrewer 

%description
An efficient tool for fitting nested mixture models based on a shared set
of atoms via Markov Chain Monte Carlo and variational inference
algorithms. Specifically, the package implements the common atoms model
(Denti et al., 2023), its finite version (similar to D'Angelo et al.,
2023), and a hybrid finite-infinite model (D'Angelo and Denti, 2024). All
models implement univariate nested mixtures with Gaussian kernels equipped
with a normal-inverse gamma prior distribution on the parameters.
Additional functions are provided to help analyze the results of the
fitting procedure. References: Denti, Camerlenghi, Guindani, Mira (2023)
<doi:10.1080/01621459.2021.1933499>, D’Angelo, Canale, Yu, Guindani (2023)
<doi:10.1111/biom.13626>, D’Angelo, Denti (2024) <doi:10.1214/24-BA1458>.

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
