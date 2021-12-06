%global __brp_check_rpaths %{nil}
%global packname  ratesci
%global packver   0.4-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Confidence Intervals for Comparisons of Binomial or Poisson Rates

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch

%description
Computes confidence intervals for the rate (or risk) difference ('RD') or
rate ratio (or relative risk, 'RR') for binomial proportions or Poisson
rates, or for odds ratio ('OR', binomial only). Also confidence intervals
for a single binomial or Poisson rate, and intervals for matched pairs.
Includes skewness-corrected asymptotic score ('SCAS') methods, which have
been developed in Laud (2017) <doi:10.1002/pst.1813> from Miettinen &
Nurminen (1985) <doi:10.1002/sim.4780040211> and Gart & Nam (1988)
<doi:10.2307/2531848>. The same score produces hypothesis tests analogous
to the test for binomial RD and RR by Farrington & Manning (1990)
<doi:10.1002/sim.4780091208>. The package also includes MOVER methods
(Method Of Variance Estimates Recovery) for all contrasts, derived from
the Newcombe method but using equal-tailed Jeffreys intervals, and
generalised for Bayesian applications incorporating prior information.
So-called 'exact' methods for strictly conservative coverage are
approximated using continuity corrections. Also includes methods for
stratified calculations (e.g. meta-analysis), either assuming fixed
effects (matching the CMH test) or incorporating stratum heterogeneity.

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
