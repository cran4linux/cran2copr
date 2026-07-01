%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clusterIV
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Clustered Jackknife Instrumental Variables Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Tools for instrumental variables estimation and inference under clustered
errors with many instruments. The current release provides the
cluster-jackknife IV estimator (CJIVE) of Frandsen, Leslie and McIntyre
(2025) <doi:10.1162/rest.a.263> for a single endogenous regressor in a
just-identified design, with cluster-robust inference: each observation's
first-stage value is fitted leaving out its entire cluster, which removes
the many-instrument bias that survives clustering. The leave-cluster-out
fits use an exact Woodbury block update -- one factorisation of the
instrument Gram matrix plus a small solve per cluster -- so the estimator
scales to large samples. A companion 'iv_compare()' reports ordinary least
squares, two-stage least squares, the observation-level jackknife and
CJIVE on a common cluster-robust standard error.

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
