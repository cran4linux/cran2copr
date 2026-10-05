%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fdb
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Frequentist Dynamic Borrowing for Hybrid-Control Survival Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-utils 

%description
Implements a class of likelihood-informed frequentist dynamic borrowing
methods for hybrid-control survival trials based on penalized Cox partial
likelihood estimation. Implements four likelihood-informed penalty
structures (precision-weighted L1, smoothed integrated-gate,
information-adaptive minimax concave penalty (MCP), and
likelihood-ratio-weighted L1), together with the adaptive lasso borrowing
approach of Li et al. (2023, <doi:10.1002/bimj.202100406>). Provides
conditional model-based standard errors and local plug-in sandwich
variance approximations, with smoothed penalties. Tools for design-stage
lambda calibration via simulation, including a two-stage coarse-fine grid
search, drift-level early stopping, and per-method tuning under both
inference types, are also provided. A simulation harness for evaluating
type I error and statistical power across population drift scenarios is
included.

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
