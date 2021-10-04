%global __brp_check_rpaths %{nil}
%global packname  EventWinRatios
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Event-Specific Win Ratios for Terminal and Non-Terminal Events

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides several confidence interval and testing procedures using
event-specific win ratios for semi-competing risks data with non-terminal
and terminal events, as developed in Yang et al. (2021, preprint).
Compared with conventional methods for survival data, these procedures are
designed to utilize more data for improved inference procedures with
semi-competing risks data. The event-specific win ratios were introduced
in Yang and Troendle (2021<doi:10.1177/1740774520972408>). In this
package, the event-specific win ratios and confidence intervals are
obtained for each event type, and several testing procedures are developed
for the global null of no treatment effect on either terminal or
non-terminal events. Furthermore, a test of proportional hazard
assumptions, under which the event-specific win ratios converge to the
hazard ratios, and a test of equal hazard ratios are provided. For
summarizing the treatment effect on all events, confidence intervals for
linear combinations of the event-specific win ratios are available using
pre-determined or data-driven weights. Asymptotic properties of these
inference procedures are discussed in Yang et al (2021, preprint). Also,
transformations are used to yield better control of the type one error
rates for moderately sized data sets.

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
