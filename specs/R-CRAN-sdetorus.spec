%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sdetorus
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tools for Toroidal Diffusions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-colorRamps 

%description
Implementation of statistical methods for the estimation of toroidal
diffusions. Several diffusive models are provided, most of them belonging
to the Langevin family of diffusions on the torus. Specifically, the
wrapped normal and von Mises processes are included, which can be seen as
toroidal analogues of the Ornstein-Uhlenbeck diffusion. A collection of
methods for approximate maximum likelihood estimation, organized in four
blocks, is given: (i) based on the exact transition probability density,
obtained as the numerical solution to the Fokker-Plank equation; (ii)
based on wrapped pseudo-likelihoods; (iii) based on specific analytic
approximations by wrapped processes; (iv) based on maximum likelihood of
the stationary densities. The package allows the replicability of the
results in García-Portugués et al. (2019) <doi:10.1007/s11222-017-9790-2>.

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
