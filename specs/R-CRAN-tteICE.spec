%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tteICE
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Treatment Effect Estimation for Time-to-Event Data with Intercurrent Events

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-survival >= 3.8.3
BuildRequires:    R-CRAN-cmprsk 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-survival >= 3.8.3
Requires:         R-CRAN-cmprsk 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-lifecycle 

%description
Analysis of treatment effects in clinical trials with time-to-event
outcomes is complicated by intercurrent events. This package implements
methods for estimating and inferring the cumulative incidence functions
for time-to-event (TTE) outcomes with intercurrent events (ICE) under the
five strategies outlined in the ICH E9 (R1) addendum, see Deng (2025)
<doi:10.1002/sim.70091>. This package can be used for analyzing data from
both randomized controlled trials and observational studies. In general,
the data involve a primary outcome event and, potentially, an intercurrent
event. Two data structures are allowed: competing risks, where only the
time to the first event is recorded, and semicompeting risks, where the
times to both the primary outcome event and intercurrent event (or
censoring) are recorded. For estimation methods, users can choose
nonparametric estimation (which does not use covariates) and
semiparametrically efficient estimation.

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
