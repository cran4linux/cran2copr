%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  progme
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extended Progression Models for Repeated Measures

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Extended progression models for repeated measures in progressive disease
clinical trials. Provides nonlinear mixed-effects progression models
(linear, plateau, Emax, exponential decay), delayed treatment onset
estimation by profile likelihood, joint longitudinal-survival models for
informative dropout, competing-risks extensions, biomarker-informed
adaptive dosing rules, and simulation-based power and sample-size
calculation. The progression-model view of treatment effects, in which
effects are characterised on the underlying disease trajectory rather than
as additive shifts on the outcome scale, follows Raket (2022)
<doi:10.1002/sim.9581>. The nonlinear mixed-effects machinery is built on
the 'nlme' implementation described by Pinheiro and Bates (2000, ISBN
978-0-387-98957-0), and the joint modelling of longitudinal and
time-to-event data follows Rizopoulos (2012, ISBN 978-1-4398-7286-4).

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
