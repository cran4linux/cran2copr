%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VARDetect
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Change Point Detection in Structural VAR Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MTS 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-sparsevar 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-stats 
Requires:         R-CRAN-MTS 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-pracma 
Requires:         R-graphics 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-sparsevar 
Requires:         R-CRAN-lattice 

%description
Implementations of Thresholded Block Segmentation Scheme (TBSS) and
Low-rank plus Sparse Two Step Procedure (LSTSP) algorithms for detecting
multiple changes in structural VAR models. The package aims to address the
problem of change point detection in piece-wise stationary VAR models,
under different settings regarding the structure of their transition
matrices (autoregressive dynamics); specifically, the following cases are
included: (i) (weakly) sparse, (ii) structured sparse, and (iii) low rank
plus sparse. It includes multiple algorithms and related extensions from
Safikhani and Shojaie (2020) <doi:10.1080/01621459.2020.1770097> and Bai,
Safikhani and Michailidis (2020) <doi:10.1109/TSP.2020.2993145>.

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
