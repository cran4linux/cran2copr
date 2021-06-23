%global __brp_check_rpaths %{nil}
%global packname  TwoArmSurvSim
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Survival Data for Randomized Clinical Trials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-blockrand 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-simsurv 
Requires:         R-CRAN-blockrand 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-simsurv 

%description
A system to simulate clinical trials with time to event endpoints. Event
simulation is based on Cox models allowing for covariates in addition to
the treatment or group factor. Specific drop-out rates (separate from
administrative censoring) can be controlled in the simulation. Other
features include stratified randomization, non-proportional hazards,
different accrual patterns, and event projection (timing to reach the
target event) based on interim data.

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
