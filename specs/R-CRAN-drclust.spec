%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  drclust
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simultaneous Clustering and (or) Dimensionality Reduction

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-pheatmap 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-pheatmap 

%description
Methods for simultaneous clustering and dimensionality reduction such as:
Double k-means, Reduced k-means, Factorial k-means, Clustering with
Disjoint PCA but also methods for exclusively dimensionality reduction:
Disjoint PCA, Disjoint FA. The statistical methods implemented refer to
the following articles: de Soete G., Carroll J. (1994) "K-means clustering
in a low-dimensional Euclidean space" <doi:10.1007/978-3-642-51175-2_24> ;
Vichi M. (2001) "Double k-means Clustering for Simultaneous Classification
of Objects and Variables" <doi:10.1007/978-3-642-59471-7_6> ; Vichi M.,
Kiers H.A.L. (2001) "Factorial k-means analysis for two-way data"
<doi:10.1016/S0167-9473(00)00064-5> ; Vichi M., Saporta G. (2009)
"Clustering and disjoint principal component analysis"
<doi:10.1016/j.csda.2008.05.028> ; Vichi M. (2017) "Disjoint factor
analysis with cross-loadings" <doi:10.1007/s11634-016-0263-9>.

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
