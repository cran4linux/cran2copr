%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sparsepca
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sparse Principal Component Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rsvd >= 2.0.0
BuildRequires:    R-CRAN-Matrix >= 1.7.0
BuildRequires:    R-methods 
Requires:         R-CRAN-rsvd >= 2.0.0
Requires:         R-CRAN-Matrix >= 1.7.0
Requires:         R-methods 

%description
Fits principal components with sparse loading vectors for interpretable
dimension reduction. Variable projection combines an orthogonal
reconstruction factor with elastic net or cardinality regularization of
the loadings. Deterministic, randomized, and robust algorithms support
exploratory analysis of high-dimensional data; the randomized algorithm
also supports sparse input matrices through implicit centering and
scaling. A robust formulation separates entrywise outliers from the
low-rank reconstruction. Regularization paths and approximate
feature-count searches reuse matrix factorizations, and prediction applies
the fitted transformation to new observations. The methods are described
in Erichson et al. (2020) <doi:10.1137/18M1211350>.

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
