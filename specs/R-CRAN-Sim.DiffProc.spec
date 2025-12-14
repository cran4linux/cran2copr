%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Sim.DiffProc
%global packver   5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation of Diffusion Processes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.30
BuildRequires:    R-CRAN-Deriv >= 3.8.0
BuildRequires:    R-parallel 
Requires:         R-CRAN-MASS >= 7.3.30
Requires:         R-CRAN-Deriv >= 3.8.0
Requires:         R-parallel 

%description
It provides users with a wide range of tools to simulate, estimate,
analyze, and visualize the dynamics of stochastic differential systems in
both forms Ito and Stratonovich. Statistical analysis with parallel Monte
Carlo and moment equations methods of SDEs <doi:10.18637/jss.v096.i02>.
Enabled many searchers in different domains to use these equations to
modeling practical problems in financial and actuarial modeling and other
areas of application, e.g., modeling and simulate of first passage time
problem in shallow water using the attractive center (Boukhetala K, 1996)
ISBN:1-56252-342-2.

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
