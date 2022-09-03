%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phaseR
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Phase Plane Analysis of One- And Two-Dimensional Autonomous ODE Systems

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-deSolve 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Performs a qualitative analysis of one- and two-dimensional autonomous
ordinary differential equation systems, using phase plane methods.
Programs are available to identify and classify equilibrium points, plot
the direction field, and plot trajectories for multiple initial
conditions. In the one-dimensional case, a program is also available to
plot the phase portrait. Whilst in the two-dimensional case, programs are
additionally available to plot nullclines and stable/unstable manifolds of
saddle points. Many example systems are provided for the user. For further
details can be found in Grayling (2014) <doi:10.32614/RJ-2014-023>.

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
