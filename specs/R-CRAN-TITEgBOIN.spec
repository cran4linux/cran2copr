%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TITEgBOIN
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Time-to-Event Dose-Finding Design for Multiple Toxicity Grades

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
In some phase I trials, the design goal is to find the dose associated
with a certain target toxicity rate or the dose with a certain weighted
sum of rates of various toxicity grades. 'TITEgBOIN' provides the set up
and calculations needed to run a dose-finding trial using bayesian optimal
interval (BOIN) (Yuan et al. (2016) <doi:10.1158/1078-0432.CCR-16-0592>),
generalized bayesian optimal interval (gBOIN) (Mu et al. (2019)
<doi:10.1111/rssc.12263>), time-to-event bayesian optimal interval
(TITEBOIN) (Lin et al. (2020) <doi:10.1093/biostatistics/kxz007>) and
time-to-event generalized bayesian optimal interval (TITEgBOIN) (Takeda et
al. (2022) <doi:10.1002/pst.2182>) designs. 'TITEgBOIN' can conduct tasks:
run simulations and get operating characteristics; determine the dose for
the next cohort; select maximum tolerated dose (MTD). These functions
allow customization of design characteristics to vary sample size, cohort
sizes, target dose limiting toxicity (DLT) rates or target normalized
equivalent toxicity score (ETS) rates to account for discrete toxicity
score, and incorporate safety and/or stopping rules.

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
