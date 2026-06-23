%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geokmeans
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Fast, Exact and Eco-Friendly k-Means Clustering Algorithms

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 

%description
A collection of fast k-means clustering algorithms under a single, uniform
interface. The core method is Geometric-k-means, a bound-free algorithm of
Sharma et al. (2026) <doi:10.1007/s10994-025-06891-1> that uses geometry
to restrict computation to the data points able to change clusters,
substantially reducing distance computations and runtime while returning
the same result as standard k-means. Also included are Lloyd's algorithm,
Elkan, Hamerly, Annulus, Exponion, and Ball k-means. All algorithms are
implemented in 'C++' via 'Rcpp' and 'RcppEigen' and return the final
centroids, optional per-point cluster assignments, and computational
statistics.

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
