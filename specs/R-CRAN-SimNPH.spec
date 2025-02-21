%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SimNPH
%global packver   0.5.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.6
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Non-Proportional Hazards

License:          BSL-1.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-miniPCH >= 0.3.0
BuildRequires:    R-CRAN-SimDesign 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-nph 
BuildRequires:    R-CRAN-nphRCT 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-miniPCH >= 0.3.0
Requires:         R-CRAN-SimDesign 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-nph 
Requires:         R-CRAN-nphRCT 
Requires:         R-CRAN-car 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-methods 
Requires:         R-CRAN-tidyr 

%description
A toolkit for simulation studies concerning time-to-event endpoints with
non-proportional hazards. 'SimNPH' encompasses functions for simulating
time-to-event data in various scenarios, simulating different trial
designs like fixed-followup, event-driven, and group sequential designs.
The package provides functions to calculate the true values of common
summary statistics for the implemented scenarios and offers common
analysis methods for time-to-event data. Helper functions for running
simulations with the 'SimDesign' package and for aggregating and
presenting the results are also included. Results of the conducted
simulation study are available in the paper: "A Comparison of Statistical
Methods for Time-To-Event Analyses in Randomized Controlled Trials Under
Non-Proportional Hazards", Klinglmüller et al. (2025)
<doi:10.1002/sim.70019>.

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
