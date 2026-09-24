%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HRRI
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Diagnostics for Soil-Plant-Microbial Redox Recovery

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-igraph >= 1.5.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-igraph >= 1.5.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 

%description
Provides diagnostic functions for integrating longitudinal soil, plant and
microbial observations during redox disturbance and recovery. Functions
calculate stoichiometric potential oxygen demand, accessible electron
capacity from explicitly supplied inventories and kinetic parameters,
recovery signatures, fixed-reference domain scores, and exploratory
multiblock scores with observation-coverage diagnostics. Memory is
represented as a holobiont state accumulating from mineralogical,
plant-acclimation and microbial-community legacies. An illustrative
simulator produces closed Fe and Mn inventories alongside synthetic
observations; its carbon, nitrogen, sulfur and oxygen budgets are not
closed and its parameters are not calibrated to field rates. Simulation
benchmarks assess agreement with a prescribed synthetic target and do not
constitute empirical validation or parameter identification. Accuracy
assessment is cluster-aware: intervals come from resampling whole
trajectories, agreement is reported as Lin's concordance coefficient
alongside correlation, and mean squared error is partitioned into bias,
variance mismatch and lack of correlation. The measured quantities follow
Sander, Hofstetter and Gorski (2015) <doi:10.1021/acs.est.5b00006> for
mediated electrochemical determination of electron-accepting and
electron-donating capacity, Kluepfel, Piepenbrock, Kappler and Sander
(2014) <doi:10.1038/ngeo2084> for regeneration of electron-accepting
capacity across repeated anoxic periods, Thompson, Chadwick, Rancourt and
Chorover (2006) <doi:10.1016/j.gca.2005.12.005> for the increase in
iron-oxide crystallinity under redox oscillation, and Keiluweit, Wanzek,
Kleber, Nico and Fendorf (2017) <doi:10.1038/s41467-017-01406-6> for
anaerobic microsites in otherwise aerobic soil. Agreement statistics
follow Lin (1989) <doi:10.2307/2532051> and Kobayashi and Salam (2000)
<doi:10.2134/agronj2000.922345x>.

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
