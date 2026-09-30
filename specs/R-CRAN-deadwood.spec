%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deadwood
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Outlier Detection via Pruning Mutual Reachability Minimum Spanning Trees

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-quitefastmst 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-quitefastmst 

%description
Implements an anomaly detection algorithm based on a dataset's mutual
reachability minimum spanning tree: 'deadwood' prunes protruding tree
segments and marks small debris as outliers; see Gagolewski (2026)
<https://deadwood.gagolewski.com/>. More precisely, tree edges with
weights greater than the detected elbow point are removed.  All the
resulting connected components whose sizes do not exceed a prespecified
threshold are deemed anomalous.  The use of a mutual reachability distance
pulls peripheral observations farther away from one another.  If the
dataset is comprised of well-separated clusters of heterogeneous
densities, an attempt to split the dataset and refine the outlierness
markers will be made. The 'Python' version of 'deadwood' is available via
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
