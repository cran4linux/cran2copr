%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  survHC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Higher Criticism Tests for Non-Proportional Hazard Deviations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Implements omnibus tests for comparing two right-censored survival samples
that are powerful against sparse departures from equal hazards, where the
hazard difference is concentrated in a small and a priori unknown subset
of the follow-up. Exact hypergeometric p-values are computed for each time
interval and aggregated with the Higher Criticism statistic of Donoho and
Jin (2004) <doi:10.1214/009053604000000265>, or alternatively with the
Berk-Jones, Fisher or minimum-p statistics. Global p-values are obtained
by permuting group labels, and the intervals driving a detection can be
recovered for diagnostic plotting. Tests accept either two samples as
vectors or the usual survival formula. The method is described in Kipnis,
Galili and Yakhini (2026) <doi:10.1093/biomet/asaf075>, and the companion
application note is Kipnis, Galili and Yakhini (2026)
<doi:10.48550/arXiv.2610.07268>.

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
