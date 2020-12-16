%global packname  uwot
%global packver   0.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.10
Release:          1%{?dist}%{?buildtag}
Summary:          The Uniform Manifold Approximation and Projection (UMAP) Method for Dimensionality Reduction

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-RcppAnnoy >= 0.0.17
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-dqrng 
Requires:         R-CRAN-RcppAnnoy >= 0.0.17
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-irlba 

%description
An implementation of the Uniform Manifold Approximation and Projection
dimensionality reduction by McInnes et al. (2018) <arXiv:1802.03426>. It
also provides means to transform new data and to carry out supervised
dimensionality reduction. An implementation of the related LargeVis method
of Tang et al. (2016) <arXiv:1602.00370> is also provided. This is a
complete re-implementation in R (and C++, via the 'Rcpp' package): no
Python installation is required. See the uwot website
(<https://github.com/jlmelville/uwot>) for more documentation and
examples.

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
