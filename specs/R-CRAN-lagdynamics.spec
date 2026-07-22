%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lagdynamics
%global packver   0.32
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.32
Release:          1%{?dist}%{?buildtag}
Summary:          Lag Sequential Analysis, Dynamics, and Lag Transition Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-cograph >= 2.3.6
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-cograph >= 2.3.6
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 

%description
A modern, tidy toolkit for lag sequential analysis and lag transition
networks of categorical event and sequence data. It provides an
accessible, unified workflow for fitting, inspecting, visualising, and
comparing lagged transition patterns, with tidy outputs throughout.
Includes confirmatory tools for uncertainty, robustness, and group
differences, including bootstrap intervals, analytic certainty, split-half
reliability, case-drop stability, permutation tests, and Bayesian group
comparisons. Supports long-format event-log import, import from common
sequence and state-sequence objects, multi-lag analysis, structural-zero
constraints, transition and initial probabilities, plotting of transition
structures, and a directed transfer-entropy measure. The lag sequential
analysis framework follows Sackett and others (1979)
<doi:10.3758/BF03205679>.

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
