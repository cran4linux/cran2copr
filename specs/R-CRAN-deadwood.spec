%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deadwood
%global packver   0.9.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Outlier Detection via Trimming of Mutual Reachability Minimum Spanning Trees

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
Implements an anomaly detection algorithm based on mutual reachability
minimum spanning trees: 'deadwood' trims protruding tree segments and
marks small debris as outliers; see Gagolewski (2026)
<https://deadwood.gagolewski.com/>. More precisely, the use of a mutual
reachability distance pulls peripheral points farther away from each
other.  Tree edges with weights beyond the detected elbow point are
removed. All the resulting connected components whose sizes are smaller
than a given threshold are deemed anomalous. The 'Python' version of
'deadwood' is available via 'PyPI'.

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
