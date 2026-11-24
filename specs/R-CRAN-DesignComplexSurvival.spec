%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DesignComplexSurvival
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation-Free Design of Complex Time-to-Event Trials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm >= 1.2.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-mvtnorm >= 1.2.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Computes the expected numbers of events, the mean, variance and covariance
of the log-rank statistic over calendar time, and the power, type I error,
required number of events, sample size, accrual duration and follow-up of
two-group time-to-event trials, without patient-level simulation. Each
group follows a multistate model (progression-free, progressed, switched,
dead, and progression-free after a switch before progression) with
piecewise constant intensities, which covers progression-free survival,
overall survival and treatment switching before, at or after progression,
with an effect of the switch on the death hazard or an accelerated failure
time effect, together with piecewise uniform accrual, piecewise
exponential dropout, a censoring of progression-free survival only,
switching that starts at a calendar time and group sequential designs with
efficacy bounds and binding or non-binding futility bounds.
Progression-free and overall survival can be tested together with a group
sequential fixed-sequence or Bonferroni procedure, the latter with
recycling of the level after a rejection as in Maurer and Bretz (2013)
<doi:10.1080/19466315.2013.807748>, using the joint distribution of the
two log-rank statistics over calendar time. For designs with one endpoint,
the expected study duration, numbers of events and enrolled patients when
the trial stops at its bounds, the conditional power at an interim
analysis, and plots of the bounds, the probabilities of stopping and the
survival functions are also given. The variance and covariance of the
log-rank score under the alternative follow Luo et al. (2019)
<doi:10.1002/sim.7975>.

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
