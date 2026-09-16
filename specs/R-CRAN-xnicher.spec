%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xnicher
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimates Ecological Niche Models Using Ellipses

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-ucminfcpp 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.1.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-RcppParallel 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-ucminfcpp 
Requires:         R-utils 

%description
Ecological niche model estimation using ellipsoidal geometry under an M
hypothesis.  Fits nine likelihood families (presence-only, weighted,
inverse-probability-weighted, skew-normal, skew-normal-weighted, skew-t,
skew-t-weighted, ncst, and ncst-weighted) via multi-start optimisation
with Sobol sequences. Methods for the optimisation of ellipses parameters
are as described in Jimenez et al. (2022)
<doi:10.1016/j.ecolmodel.2021.109823>.

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
