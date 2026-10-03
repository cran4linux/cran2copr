%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  timesift
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Learn Predictive Representations of Time-Varying Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Fits and compares representations of time-varying data against a
prediction target. Given a table of targets and a table of time-stamped
series belonging to them, it builds each candidate representation, from
the record unreduced through a calendar grain such as a week or a month to
a lookback anchored on each target, fits the requested learners on each,
scores every candidate on one set of held-out folds, and stacks the
out-of-fold predictions into an ensemble. Calendar-aware binning keeps a
bin a real week or month rather than a fixed block of hours. Learners,
response heads and metrics are registered rather than hard-coded, so
adding one is a registration and not a fork of the fitting code. The
penalised baseline is an elastic net fitted by cyclic coordinate descent
along a warm-started path, following Friedman, Hastie and Tibshirani
(2010) <doi:10.18637/jss.v033.i01>. The shipped default is
presence-absence with a joint multi-label head scored by the true skill
statistic of Allouche, Tsoar and Kadmon (2006)
<doi:10.1111/j.1365-2664.2006.01214.x>, the setting used for species
distribution modelling from microclimate loggers.

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
