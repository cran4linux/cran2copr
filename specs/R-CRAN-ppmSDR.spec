%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ppmSDR
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized Principal Machine for Sufficient Dimension Reduction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-grpreg 
BuildRequires:    R-CRAN-energy 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-grpreg 
Requires:         R-CRAN-energy 

%description
A unified, computation-friendly framework for penalized principal machines
(P2M), a class of sparse sufficient dimension reduction (SDR) estimators
for regression and binary classification. Principal machines (PM) estimate
the central subspace by solving a family of convex-loss problems over
several cutoffs; their penalized counterparts (P2M) add a row-group
sparsity penalty so that dimension reduction and variable selection are
performed simultaneously. All estimators are fitted by a single group
coordinate descent (GCD) algorithm that accommodates least squares,
logistic, asymmetric least squares, L2-hinge, hinge (support vector
machine, SVM) and quantile losses, together with the least absolute
shrinkage and selection operator (LASSO), the smoothly clipped absolute
deviation (SCAD) penalty and the minimax concave penalty (MCP). Methods
are described in Li, Artemiou and Li (2011) <doi:10.1214/11-AOS932>, Shin
and Artemiou (2017) <doi:10.1016/j.csda.2016.12.003>, Artemiou, Dong and
Shin (2021) <doi:10.1016/j.patcog.2020.107768> and Breheny and Huang
(2015) <doi:10.1007/s11222-013-9424-2>.

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
