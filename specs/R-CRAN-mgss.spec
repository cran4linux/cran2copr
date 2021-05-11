%global packname  mgss
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Matrix-Free Multigrid Preconditioner for Spline Smoothing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Matrix >= 1.2
BuildRequires:    R-CRAN-statmod >= 1.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-combinat >= 0.0.8
Requires:         R-CRAN-Matrix >= 1.2
Requires:         R-CRAN-statmod >= 1.1
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-combinat >= 0.0.8

%description
Data smoothing with penalized splines is a popular method and is well
established for one- or two-dimensional covariates. The extension to
multiple covariates is straightforward but suffers from exponentially
increasing memory requirements and computational complexity. This toolbox
provides a matrix-free implementation of a conjugate gradient (CG) method
for the regularized least squares problem resulting from tensor product
B-spline smoothing with multivariate and scattered data. It further
provides matrix-free preconditioned versions of the CG-algorithm where the
user can choose between a simpler diagonal preconditioner and an advanced
geometric multigrid preconditioner. The main advantage is that all
algorithms are performed matrix-free and therefore require only a small
amount of memory. For further detail see Siebenborn & Wagner (2021).

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
