%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qicharts2
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quality Improvement Charts

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-scales 
Requires:         R-stats 

%description
Functions for making run charts, Shewhart control charts and Pareto charts
for continuous quality improvement. Included control charts are: I, MR,
Xbar, S, T, C, U, U', P, P', and G charts. Non-random variation in the
form of minor to moderate persistent shifts in data over time is
identified by the Anhoej rules for unusually long runs and unusually few
crossing [Anhoej, Olesen (2014) <doi:10.1371/journal.pone.0113825>].
Non-random variation in the form of larger, possibly transient, shifts is
identified by Shewhart's 3-sigma rule [Mohammed, Worthington, Woodall
(2008) <doi:10.1136/qshc.2004.012047>].

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
