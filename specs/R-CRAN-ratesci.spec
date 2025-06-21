%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ratesci
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Confidence Intervals and Tests for Comparisons of Binomial Proportions or Poisson Rates

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch

%description
Computes confidence intervals for binomial or Poisson rates and their
differences or ratios. Including the rate (or risk) difference ('RD') or
rate ratio (or relative risk, 'RR') for binomial proportions or Poisson
rates, and odds ratio ('OR', binomial only). Also confidence intervals for
RD, RR or OR for paired binomial data, and estimation of a proportion from
clustered binomial data. Includes skewness-corrected asymptotic score
('SCAS') methods, which have been developed in Laud (2017)
<doi:10.1002/pst.1813> from Miettinen and Nurminen (1985)
<doi:10.1002/sim.4780040211> and Gart and Nam (1988)
<doi:10.2307/2531848>, and in Laud (2025, under review) for paired
proportions. The same score produces hypothesis tests that are improved
versions of the non-inferiority test for binomial RD and RR by Farrington
and Manning (1990) <doi:10.1002/sim.4780091208>, or a generalisation of
the McNemar test for paired data. The package also includes MOVER methods
(Method Of Variance Estimates Recovery) for all contrasts, derived from
the Newcombe method but with options to use equal-tailed intervals in
place of the Wilson score method, and generalised for Bayesian
applications incorporating prior information. So-called 'exact' methods
for strictly conservative coverage are approximated using continuity
adjustments, and the amount of adjustment can be selected to avoid
over-conservative coverage.  Also includes methods for stratified
calculations (e.g. meta-analysis), either with fixed effect assumption
(matching the CMH test) or incorporating stratum heterogeneity.

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
