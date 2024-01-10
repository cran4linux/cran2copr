%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pttstability
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Particle-Takens Stability

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-stats 

%description
Includes a collection of functions presented in "Measuring stability in
ecological systems without static equilibria" by Clark et al. (2022)
<doi:10.1002/ecs2.4328> in Ecosphere. These can be used to estimate the
parameters of a stochastic state space model (i.e. a model where a time
series is observed with error). The goal of this package is to estimate
the variability around a deterministic process, both in terms of
observation error - i.e. variability due to imperfect observations that
does not influence system state - and in terms of process noise - i.e.
stochastic variation in the actual state of the process. Unlike classical
methods for estimating variability, this package does not necessarily
assume that the deterministic state is fixed (i.e. a fixed-point
equilibrium), meaning that variability around a dynamic trajectory can be
estimated (e.g. stochastic fluctuations during predator-prey dynamics).

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
