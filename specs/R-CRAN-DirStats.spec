%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DirStats
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Methods for Directional Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Bessel 
BuildRequires:    R-CRAN-movMF 
Requires:         R-CRAN-Bessel 
Requires:         R-CRAN-movMF 

%description
Nonparametric kernel density estimation and bandwidth selection for
directional data on the hypersphere S^q, q >= 1. Implements the kernel
density estimator of Bai et al. (1988) <doi:10.1016/0047-259X(88)90113-3>
in kde_dir(), the likelihood and least squares cross-validation bandwidth
selectors of Hall et al. (1987) <doi:10.1093/biomet/74.4.751> in
bw_dir_lcv() and bw_dir_lscv(), and the rule-of-thumb and plug-in
selectors of García-Portugués (2013) <doi:10.1214/13-EJS821> in
bw_dir_rot(), bw_dir_ami(), and bw_dir_emi(). Also fits mixtures of von
Mises-Fisher distributions with bic_vmf_mix(), integrates on S^q, and
provides fast stable evaluations of the log-Bessel function and the von
Mises-Fisher normalizing constant for large orders and concentrations.

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
