%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sphunif
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Uniformity Tests on the Circle, Sphere, and Hypersphere

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-rotasym 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-rotasym 

%description
Implementation of uniformity tests on the circle and (hyper)sphere. The
main function of the package is unif_test(), which conveniently collects
more than 35 tests for assessing uniformity on S^{p-1} = {x in R^p : ||x||
= 1}, p >= 2. The test statistics are implemented in the unif_stat()
function, which allows computing several statistics for different samples
within a single call, thus facilitating Monte Carlo experiments.
Furthermore, the unif_stat_MC() function allows parallelizing them in a
simple way. The asymptotic null distributions of the statistics are
available through the function unif_stat_distr(). The core of 'sphunif' is
coded in C++ by relying on the 'Rcpp' package. The package also provides
several novel datasets and gives the replicability for the data
applications/simulations in García-Portugués et al. (2021)
<doi:10.1007/978-3-030-69944-4_12>, García-Portugués et al. (2023)
<doi:10.3150/21-BEJ1454>, García-Portugués et al. (2024)
<doi:10.48550/arXiv.2108.09874>, and Fernández-de-Marcos and
García-Portugués (2024) <doi:10.48550/arXiv.2405.13531>.

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
