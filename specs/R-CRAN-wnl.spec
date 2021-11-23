%global __brp_check_rpaths %{nil}
%global packname  wnl
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          1%{?dist}%{?buildtag}
Summary:          Minimization Tool for Pharmacokinetic-Pharmacodynamic Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-numDeriv 

%description
This is a set of minimization tools (maximum likelihood estimation and
least square fitting) to solve examples in the Johan Gabrielsson and Dan
Weiner's book "Pharmacokinetic and Pharmacodynamic Data Analysis -
Concepts and Applications" 5th ed. (ISBN:9198299107). Examples include
linear and nonlinear compartmental model, turn-over model, single or
multiple dosing bolus/infusion/oral models, allometry, toxicokinetics,
reversible metabolism, in-vitro/in-vivo extrapolation, enterohepatic
circulation, metabolite modeling, Emax model, inhibitory model, tolerance
model, oscillating response model, enantiomer interaction model, effect
compartment model, drug-drug interaction model, receptor occupancy model,
and rebound phenomena model.

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
