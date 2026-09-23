%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FSHybridPLS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hybrid Penalized Partial Least Squares for Mixed Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fda >= 6.1.3
BuildRequires:    R-stats 
Requires:         R-CRAN-fda >= 6.1.3
Requires:         R-stats 

%description
Fits Penalized Partial Least Squares (PLS) regression when predictors are
hybrid objects that combine functional curves (infinite-dimensional 'fda'
objects) and scalar covariates (finite-dimensional numeric matrices). The
package treats a hybrid predictor as an element of a product Hilbert space
formed by the functional and Euclidean components, and implements the
arithmetic (addition, scalar multiplication, and inner products, including
roughness-penalized inner products) needed to run penalized PLS directly
in that space. The algorithm extracts latent components that maximize
covariance with a scalar response while penalizing roughness of the
estimated functional coefficient curves. Helpers are included for
constructing hybrid predictors, two-step within- and between-modality
normalization, train/test splitting, synthetic data generation,
cross-validated component selection, and prediction. The method is
described in Mun and Jang (2026) <doi:10.48550/arXiv.2601.16364>.

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
