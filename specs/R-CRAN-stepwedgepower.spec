%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stepwedgepower
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation-Based Power Evaluation for Stepped-Wedge Cluster Randomized Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lifecycle 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-utils 

%description
Provides simulation-based power, type I error, and operating-
characteristic evaluation for stepped-wedge cluster randomized trials.
General binary-outcome designs support arbitrary crossover schedules,
unequal clusters per sequence, secular trends, flexible cluster-period
sizes, reproducible parallel execution, sensitivity grids, and mixed-model
diagnostics. A component-based engine supports the four treatment states
Control, A, B, and A+B under arbitrary asynchronous schedules, including
structurally unobserved cluster-periods, withdrawal, reintroduction,
wash-in delays, user-defined carryover decay, component main effects, an
A-by-B interaction, estimability audits, multiplicity adjustment,
conditional and failure-aware power, and explicit classification of hard
model errors, nonconvergence, non-finite contrasts, singular fits, and
successful fits. A batch-aware interface represents classic and batched
stepped-wedge designs with delayed cluster initiation, structurally
unobserved cluster-periods, and calendar-time, time-on-trial, or separate
batch-specific time effects, following Kasza, Bowden, Hooper and Forbes
(2022) <doi:10.1002/sim.9438>. The cumulative Control-to-A-to-A+B
interface from earlier versions remains available. The design and
mixed-effects analysis follow Hussey and Hughes (2007)
<doi:10.1016/j.cct.2006.05.007>. Intraclass correlations for binary
outcomes are converted to random-intercept standard deviations on the
latent scale of the logistic-normal model, as reviewed by Eldridge,
Ukoumunne and Carlin (2009) <doi:10.1111/j.1751-5823.2009.00092.x>. Monte
Carlo uncertainty is reported using exact intervals from Clopper and
Pearson (1934) <doi:10.1093/biomet/26.4.404>.

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
