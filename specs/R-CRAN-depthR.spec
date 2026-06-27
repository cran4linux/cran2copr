%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  depthR
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Depth Functions for General Dimension

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-RcppParallel >= 5.0.0
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-stats 
Requires:         R-graphics 

%description
Efficient computation of multivariate statistical depth functions in
arbitrary dimension d. Implements Mahalanobis depth, Tukey (halfspace)
depth, Liu simplicial depth (via adaptive Monte Carlo), projection depth,
and spatial depth. Provides depth-based medians, central regions, outlier
detection, and depth-depth plots. 'C++' backends via 'Rcpp' and
'RcppEigen' ensure performance at large n and d. References: Liu (1990)
<doi:10.1214/aos/1176347507>, Zuo and Serfling (2000)
<doi:10.1214/aos/1016218226>, Vardi and Zhang (2000)
<doi:10.1073/pnas.97.4.1423>.

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
