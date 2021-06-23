%global __brp_check_rpaths %{nil}
%global packname  RJcluster
%global packver   2.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          RJ Clustering Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-profvis 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-infotheo 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-profvis 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-foreach 

%description
Clustering algorithm for high dimensional data. This algorithm is ideal
for data where N << P. Assuming that P feature measurements on N objects
are arranged in an N×P matrix X, this package provides clustering based on
the left Gram matrix XX^T. When the P-dimensional feature vectors of
objects are drawn independently from a K distinct mixture distribution,
the N-dimensional rows of the modified Gram matrix XX^T/P converges almost
surely to K distinct cluster means. This transformation/projection thus
allows the clusters to be tighter with order of P.  To simulate data, type
"help('simulate_HD_data')" and to learn how to use the clustering
algorithm, type "help('RJclust')".

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
