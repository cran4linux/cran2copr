%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fdacluster
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Joint Clustering and Alignment of Functional Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-fdasrvf 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-fdasrvf 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 

%description
Implementations of the k-means, hierarchical agglomerative and DBSCAN
clustering methods for functional data which allows for jointly aligning
and clustering curves. It supports functional data defined on
one-dimensional domains but possibly evaluating in multivariate codomains.
It supports functional data defined in arrays but also via the 'fd' and
'funData' classes for functional data defined in the 'fda' and 'funData'
packages respectively. It currently supports shift, dilation and affine
warping functions for functional data defined on the real line and uses
the SRVF framework to handle boundary-preserving warping for functional
data defined on a specific interval. Main reference for the k-means
algorithm: Sangalli L.M., Secchi P., Vantini S., Vitelli V. (2010) "k-mean
alignment for curve clustering" <doi:10.1016/j.csda.2009.12.008>. Main
reference for the SRVF framework: Tucker, J. D., Wu, W., & Srivastava, A.
(2013) "Generative models for functional data using phase and amplitude
separation" <doi:10.1016/j.csda.2012.12.001>.

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
