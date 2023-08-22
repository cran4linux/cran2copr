%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  elastes
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Elastic Full Procrustes Means for Sparse and Irregular Planar Curves

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-elasdics 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-sparseFLMM 
BuildRequires:    R-CRAN-orthogonalsplinebasis 
Requires:         R-CRAN-elasdics 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-splines 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-sparseFLMM 
Requires:         R-CRAN-orthogonalsplinebasis 

%description
Provides functions for the computation of functional elastic shape means
over sets of open planar curves. The package is particularly suitable for
settings where these curves are only sparsely and irregularly observed. It
uses a novel approach for elastic shape mean estimation, where planar
curves are treated as complex functions and a full Procrustes mean is
estimated from the corresponding smoothed Hermitian covariance surface.
This is combined with the methods for elastic mean estimation proposed in
Steyer, Stöcker, Greven (2022) <doi:10.1111/biom.13706>. See Stöcker et.
al. (2022) <arXiv:2203.10522> for details.

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
