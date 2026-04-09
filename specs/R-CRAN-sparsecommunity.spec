%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sparsecommunity
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spectral Community Detection for Sparse Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-RSpectra 
Requires:         R-stats 

%description
Implements spectral clustering algorithms for community detection in
sparse networks under the stochastic block model ('SBM') and
degree-corrected stochastic block model ('DCSBM'), following the methods
of Lei and Rinaldo (2015) <doi:10.1214/14-AOS1274>. Provides a regularized
normalized Laplacian embedding, spherical k-median clustering for 'DCSBM',
standard k-means for 'SBM', simulation utilities for both models, and a
misclustering rate evaluation metric. Also includes the 'NCAA' college
football network of Girvan and Newman (2002) <doi:10.1073/pnas.122653799>
as a benchmark dataset, and the Bethe-Hessian community number estimator
of Hwang (2023) <doi:10.1080/01621459.2023.2223793>.

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
