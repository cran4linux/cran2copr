%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesSurveillance
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Surveillance Methods for Healthcare Performance Monitoring

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Provides Bayesian surveillance methods for prospective monitoring of
healthcare performance, patient safety, and clinical quality indicators.
The package implements beta-binomial monitoring for binary outcomes,
gamma-Poisson monitoring for count outcomes, posterior predictive alert
probabilities, Bayesian early-warning signal detection, risk-adjusted
surveillance, simulation tools, decision-support methods, and graphical
summaries. These methods support continuous performance monitoring and
timely detection of adverse trends in healthcare systems. The methodology
is motivated by established risk-adjusted monitoring, sequential
surveillance, and healthcare quality-improvement frameworks
<doi:10.1093/biostatistics/1.4.441>, <doi:10.1002/sim.1546>,
<doi:10.1136/bmjqs.2008.031831>, and <doi:10.1136/bmjqs-2016-005526>.

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
