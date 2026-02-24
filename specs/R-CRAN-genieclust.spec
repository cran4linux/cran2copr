%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  genieclust
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Genie: Fast and Robust Hierarchical Clustering

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-deadwood 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-deadwood 

%description
Genie is a robust hierarchical clustering algorithm (Gagolewski,
Bartoszuk, Cena, 2016 <DOI:10.1016/j.ins.2016.05.003>). 'genieclust' is
its faster, more capable implementation (Gagolewski, 2021
<DOI:10.1016/j.softx.2021.100722>).  It enables clustering with respect to
mutual reachability distances, allowing it to act as an alternative to
'HDBSCAN*' that can identify any number of clusters or their entire
hierarchy.  When combined with the 'deadwood' package, it can act as an
outlier detector.  Additional package features include the Gini and
Bonferroni inequality indices, external cluster validity measures (e.g.,
the normalised clustering accuracy, the adjusted Rand index, the
Fowlkes-Mallows index, and normalised mutual information), and internal
cluster validity indices (e.g., the Calinski-Harabasz, Davies-Bouldin,
Ball-Hall, Silhouette, and generalised Dunn indices). The 'Python' version
of 'genieclust' is available via 'PyPI'.

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
