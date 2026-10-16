%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  recruitlag
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Can Episodic Recruitment be a Delayed Consequence of Continuous Reproduction?

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-utils 

%description
Tests whether an episodic recruitment record can be the delayed
consequence of a reproductive record, under any distributed lag. A delay
is a convolution, and a convolution is a weighted average, so the
concentration in time of expected recruitment can never exceed that of
reproduction: reproduction's own concentration is a ceiling. The package
computes that ceiling by searching families of lag weights (pure delays,
windows, geometric decay and Dirichlet draws), calibrates the pooled
comparison against negative-binomial counts to show what it can and cannot
refute, and runs the host-level (replicate-unit) test in which the null is
the lag hypothesis exactly as it is asserted: expected recruitment on each
unit is that unit's own lagged reproduction, scaled to its own total.
Uncertainty on the exceedance comes by three routes, a cluster bootstrap
over units, a Bayesian bootstrap (Rubin 1981 <doi:10.1214/aos/1176345338>)
and a negative-binomial model of the counts fitted with 'Stan' through
'cmdstanr'; recruit_triage() asks whether a first sighting is a recruit or
a plant returning from dormancy. Plotting functions draw the ceiling
strip, the lag profiles against the observed counts, the calibration and a
forest plot of the intervals. The census data on the epiphytic orchid
Lepanthes eltoroensis analysed in the companion paper are included.

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
