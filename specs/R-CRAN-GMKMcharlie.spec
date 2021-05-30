%global packname  GMKMcharlie
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Unsupervised Gaussian Mixture and Minkowski and Spherical K-Means with Constraints

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-RcppParallel 

%description
High performance trainers for parameterizing and clustering weighted data.
The Gaussian mixture (GM) module includes the conventional EM (expectation
maximization) trainer, the component-wise EM trainer, the
minimum-message-length EM trainer by Figueiredo and Jain (2002)
<doi:10.1109/34.990138>. These trainers accept additional constraints on
mixture weights, covariance eigen ratios and on which mixture components
are subject to update. The K-means (KM) module offers clustering with the
options of (i) deterministic and stochastic K-means++ initializations,
(ii) upper bounds on cluster weights (sizes), (iii) Minkowski distances,
(iv) cosine dissimilarity, (v) dense and sparse representation of data
input. The package improved the typical implementations of GM and KM
algorithms in various aspects. It is carefully crafted in multithreaded
C++ for modeling large data for industry use.

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
