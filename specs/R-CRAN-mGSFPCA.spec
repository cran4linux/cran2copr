%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mGSFPCA
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Functional Principal Components from Sparse Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Metrics 

%description
Implements functional principal component analysis (FPCA) for univariate
and multivariate sparse functional data. The package estimates
eigenfunctions, eigenvalues, and error variance simultaneously via maximum
likelihood estimation (MLE), using a spline basis representation of the
eigenfunctions. Orthonormality of the estimated eigenfunctions is enforced
through a modified Gram-Schmidt (MGS) orthogonalization procedure applied
iteratively during estimation, avoiding direct optimization over the
Stiefel manifold and improving numerical stability. The optimal number of
basis functions and principal components is selected via an Akaike
Information Criterion (AIC)-type criterion, supporting both a full
grid-search strategy and a computationally efficient sequential selection
approach. Principal component scores are estimated by conditional
expectation, enabling reconstruction of individual trajectories over the
entire domain from sparse observations. Pointwise confidence intervals for
reconstructed trajectories are also provided. Methods are described in
Mbaka, Cao and Carey (2026) <doi:10.48550/arXiv.2603.18833> and Mbaka and
Carey (2026) <doi:10.48550/arXiv.2603.19799>.

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
