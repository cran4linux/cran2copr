%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  genieclust
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Fast and Robust Hierarchical Clustering with Noise Points Detection

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-stats 
Requires:         R-utils 

%description
A retake on the Genie algorithm (Gagolewski, 2021
<DOI:10.1016/j.softx.2021.100722>) - a robust hierarchical clustering
method (Gagolewski, Bartoszuk, Cena, 2016
<DOI:10.1016/j.ins.2016.05.003>). Now faster and more memory efficient;
determining the whole hierarchy for datasets of 10M points in low
dimensional Euclidean spaces or 100K points in high-dimensional ones takes
only 1-2 minutes. Allows clustering with respect to mutual reachability
distances so that it can act as a noise point detector or a robustified
version of 'HDBSCAN*' (that is able to detect a predefined number of
clusters and hence it does not dependent on the somewhat fragile 'eps'
parameter). The package also features an implementation of inequality
indices (the Gini, Bonferroni index), external cluster validity measures
(e.g., the normalised clustering accuracy and partition similarity scores
such as the adjusted Rand, Fowlkes-Mallows, adjusted mutual information,
and the pair sets index), and internal cluster validity indices (e.g., the
Calinski-Harabasz, Davies-Bouldin, Ball-Hall, Silhouette, and generalised
Dunn indices). See also the 'Python' version of 'genieclust' available on
'PyPI', which supports sparse data, more metrics, and even larger
datasets.

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
