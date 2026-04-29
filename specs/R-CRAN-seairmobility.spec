%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  seairmobility
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mobility-Based SEAIR Epidemic Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve >= 1.30
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-deSolve >= 1.30
Requires:         R-stats 
Requires:         R-graphics 

%description
Tools for simulating, analysing, and fitting mobility-based SEAIR
(Susceptible-Exposed-Asymptomatic-Infectious-Recovered) compartmental
epidemic models with heterogeneous individual mobility. Each individual
carries a fixed mobility trait that scales susceptibility and
infectiousness through a rank-one kernel, extending the mobility-based
compartmental framework of Jiang et al. (2025) <doi:10.1137/24M1691557> by
adding a latent stage and a behavioural split between asymptomatic and
symptomatic infectiousness. Provides a numerical solver for the underlying
partial differential equation system, closed-form computation of the basic
reproduction number R0 and the final epidemic size, and a parametric
least-squares routine for recovering the mobility distribution from an
observed aggregate symptomatic time series.

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
