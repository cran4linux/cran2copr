%global __brp_check_rpaths %{nil}
%global packname  EleChemr
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Electrochemical Reactions Simulation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ggplot2 

%description
Digital simulation of electrochemical processes. Each function allows for
implicit and explicit solution of the differential equation using methods
like Euler, Backwards implicit, Runge Kutta 4, Crank Nicholson and
Backward differentiation formula as well as different number of points for
derivative approximation. Several electrochemical processes can be
simulated such as: Chronoamperometry, Potential Step, Linear Sweep, Cyclic
Voltammetry, Cyclic Voltammetry with electrochemical reaction followed by
chemical reaction (EC mechanism) and CV with two following electrochemical
reaction (EE mechanism). In update 1.1.0 has been added a general purpose
CV function that allow to simulate up to 4 EE mechanism combined with
chemical reaction for each species.Update 1.2.0 improved the accuracy of
the measurements and allow personalized data resolution for simulation.
Bibliography regarding this methods can be found in the following texts.
Dieter Britz, Jorg Strutwolf (2016) <ISBN:978-3-319-30292-8>. Allen J.
Bard, Larry R. Faulkner (2000) <ISBN:978-0-471-04372-0>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
