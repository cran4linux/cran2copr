%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  genieclust
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast and Robust Hierarchical Clustering with Noise Point Detection

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-quitefastmst 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-quitefastmst 

%description
The Genie algorithm (Gagolewski, 2021 <DOI:10.1016/j.softx.2021.100722>)
is a robust and outlier-resistant hierarchical clustering method
(Gagolewski, Bartoszuk, Cena, 2016 <DOI:10.1016/j.ins.2016.05.003>). This
package features its faster and more powerful version. It allows
clustering with respect to mutual reachability distances, enabling it to
act as a noise point detector or a version of 'HDBSCAN*' that can identify
a predefined number of clusters. The package also features an
implementation of the Gini and Bonferroni inequality indices, external
cluster validity measures (e.g., the normalised clustering accuracy, the
adjusted Rand index, the Fowlkes-Mallows index, and normalised mutual
information), and internal cluster validity indices (e.g., the
Calinski-Harabasz, Davies-Bouldin, Ball-Hall, Silhouette, and generalised
Dunn indices). The 'Python' version of 'genieclust' is available via
'PyPI'.

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
