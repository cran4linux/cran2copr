%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  achieveGap
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Modeling Achievement Gap Trajectories with Hierarchical Penalized Splines

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-mgcv >= 1.9.0
BuildRequires:    R-CRAN-lme4 >= 1.1.0
Requires:         R-CRAN-MASS >= 7.3.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-mgcv >= 1.9.0
Requires:         R-CRAN-lme4 >= 1.1.0

%description
Implements a hierarchical penalized spline framework for estimating
achievement gap trajectories in longitudinal educational data. The
achievement gap between two groups (e.g., low versus high socioeconomic
status) is modeled directly as a smooth function of grade while the
baseline trajectory is estimated simultaneously within a mixed-effects
model. Smoothing parameters are selected using restricted maximum
likelihood (REML), and simultaneous confidence bands with correct joint
coverage are constructed using posterior simulation. The package also
includes functions for simulation-based benchmarking, visualization of gap
trajectories, and hypothesis testing for global and grade-specific
differences. The modeling framework builds on penalized spline methods
(Eilers and Marx, 1996, <doi:10.1214/ss/1038425655>) and generalized
additive modeling approaches (Wood, 2017, <doi:10.1201/9781315370279>),
with uncertainty quantification following Marra and Wood (2012,
<doi:10.1111/j.1467-9469.2011.00760.x>).

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
