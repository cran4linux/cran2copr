%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gsDesignNB
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Sample Size and Simulation for Negative Binomial Outcomes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-gsDesign 
BuildRequires:    R-CRAN-simtrial 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-gsDesign 
Requires:         R-CRAN-simtrial 
Requires:         R-stats 
Requires:         R-CRAN-MASS 

%description
Provides tools for planning and simulating recurrent event trials with
overdispersed count endpoints analyzed using negative binomial (or
Poisson) rate models. Implements sample size and power calculations for
fixed designs with variable accrual, dropout, maximum follow-up, and event
gaps, including methods of Zhu and Lakkis (2014) <doi:10.1002/sim.5947>
and Friede and Schmidli (2010) <doi:10.3414/ME09-02-0060>. Supports group
sequential designs by adding calendar-time analysis schedules compatible
with the 'gsDesign' package and by estimating blinded information at
interim looks. Includes simulation utilities for recurrent events
(including seasonal rates), interim data truncation, and Wald-based
inference for treatment rate ratios.

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
