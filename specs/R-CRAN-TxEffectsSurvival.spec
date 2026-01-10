%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TxEffectsSurvival
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Treatment Effect Inference for Terminal and Non-Terminal Events under Competing Risks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides several confidence interval and testing procedures, based on
either semiparametric (using event-specific win ratios) or nonparametric
measures, including the ratio of integrated cumulative hazard (RICH) and
the ratio of integrated transformed cumulative hazard (RITCH), for
treatment effect inference with terminal and non-terminal events under
competing risks. The semiparametric results were developed in Yang et al.
(2022 <doi:10.1002/sim.9266>), and the nonparametric results were
developed in Yang (2025 <doi:10.1002/sim.70205>). For comparison, results
for the win ratio (Finkelstein and Schoenfeld 1999
<doi:10.1002/(SICI)1097-0258(19990615)18:11%%3C1341::AID-SIM129%%3E3.0.CO;2-7>),
Pocock et al. 2012 <doi:10.1093/eurheartj/ehr352>, and Bebu and Lachin
2016 <doi:10.1093/biostatistics/kxv032>) are included. The package also
supports univariate survival analysis with a single event. In this
package, effect size estimates and confidence intervals are obtained for
each event type, and several testing procedures are implemented for the
global null hypothesis of no treatment effect on either terminal or
non-terminal events. Furthermore, a test of proportional hazards
assumptions, under which the event-specific win ratios converge to hazard
ratios, and a test of equal hazard ratios, are provided. For summarizing
the treatment effect across all events, confidence intervals for linear
combinations of the event-specific win ratios, RICH, or RITCH are
available using pre-determined or data-driven weights. Asymptotic
properties of these inference procedures are discussed in Yang et al.
(2022 <doi:10.1002/sim.9266>) and Yang (2025 <doi:10.1002/sim.70205>).

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
