%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Kmedians
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          K-Medians

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-genieclust 
BuildRequires:    R-CRAN-Gmedian 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-capushe 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-genieclust 
Requires:         R-CRAN-Gmedian 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-capushe 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 

%description
Online, Semi-online, and Offline K-medians algorithms are given. For both
methods, the algorithms can be initialized randomly or with the help of a
robust hierarchical clustering. The number of clusters can be selected
with the help of a penalized criterion. We provide functions to provide
robust clustering. Function gen_K() enables to generate a sample of data
following a contaminated Gaussian mixture. Functions Kmedians() and
Kmeans() consists in a K-median and a K-means algorithms while Kplot()
enables to produce graph for both methods. Cardot, H., Cenac, P. and Zitt,
P-A. (2013). "Efficient and fast estimation of the geometric median in
Hilbert spaces with an averaged stochastic gradient algorithm". Bernoulli,
19, 18-43. <doi:10.3150/11-BEJ390>. Cardot, H. and Godichon-Baggioni, A.
(2017). "Fast Estimation of the Median Covariation Matrix with Application
to Online Robust Principal Components Analysis". Test, 26(3), 461-480
<doi:10.1007/s11749-016-0519-x>. Godichon-Baggioni, A. and Surendran, S.
"A penalized criterion for selecting the number of clusters for K-medians"
<arXiv:2209.03597> Vardi, Y. and Zhang, C.-H. (2000). "The multivariate
L1-median and associated data depth". Proc. Natl. Acad. Sci. USA,
97(4):1423-1426. <doi:10.1073/pnas.97.4.1423>.

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
