%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cmfrec
%global packver   3.5.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Collective Matrix Factorization for Recommender Systems

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Collective matrix factorization (a.k.a. multi-view or multi-way
factorization, Singh, Gordon, (2008) <doi:10.1145/1401890.1401969>) tries
to approximate a (potentially very sparse or having many missing values)
matrix 'X' as the product of two low-dimensional matrices, optionally
aided with secondary information matrices about rows and/or columns of
'X', which are also factorized using the same latent components. The
intended usage is for recommender systems, dimensionality reduction, and
missing value imputation. Implements extensions of the original model
(Cortes, (2018) <arXiv:1809.00366>) and can produce different
factorizations such as the weighted 'implicit-feedback' model (Hu, Koren,
Volinsky, (2008) <doi:10.1109/ICDM.2008.22>), the
'weighted-lambda-regularization' model, (Zhou, Wilkinson, Schreiber, Pan,
(2008) <doi:10.1007/978-3-540-68880-8_32>), or the enhanced model with
'implicit features' (Rendle, Zhang, Koren, (2019) <arXiv:1905.01395>),
with or without side information. Can use gradient-based procedures or
alternating-least squares procedures (Koren, Bell, Volinsky, (2009)
<doi:10.1109/MC.2009.263>), with either a Cholesky solver, a faster
conjugate gradient solver (Takacs, Pilaszy, Tikk, (2011)
<doi:10.1145/2043932.2043987>), or a non-negative coordinate descent
solver (Franc, Hlavac, Navara, (2005) <doi:10.1007/11556121_50>),
providing efficient methods for sparse and dense data, and mixtures
thereof. Supports L1 and L2 regularization in the main models, offers
alternative most-popular and content-based models, and implements
functionality for cold-start recommendations and imputation of 2D data.

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
