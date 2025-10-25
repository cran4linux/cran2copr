%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ETAS
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Modeling Earthquake Data Using 'ETAS' Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-goftest 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-CRAN-fields 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-goftest 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-spatstat.random 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-fields 

%description
Fits the space-time Epidemic Type Aftershock Sequence ('ETAS') model to
earthquake catalogs using a stochastic 'declustering' approach. The 'ETAS'
model is a 'spatio-temporal' marked point process model and a special case
of the 'Hawkes' process. The package is based on a Fortran program by
'Jiancang Zhuang' (available at
<https://bemlar.ism.ac.jp/zhuang/software.html>), which is modified and
translated into C++ and C such that it can be called from R. Parallel
computing with 'OpenMP' is possible on supported platforms.

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
