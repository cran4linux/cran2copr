%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lagdynamics
%global packver   0.35.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.35.0
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
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-cograph >= 2.3.6
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements lag sequential analysis of categorical event and sequence data.
For each ordered pair of states it tests whether one state follows another
at a given lag more or less often than expected under independence,
reporting adjusted residuals, transitional probabilities and Yule's Q in
tidy data frames. Five test engines are provided (classical, two-cell,
bidirectional, parallel dominance and non-parallel dominance). Transitions
can be evaluated with bootstrap intervals, analytic certainty, split-half
reliability, case-drop stability and permutation tests, and groups
compared by permutation or by a Bayesian Dirichlet-multinomial contrast.
Supports long-format event logs, sequence objects, multiple lags,
structural zeros, transition and initial probabilities, plots of lag
transition networks, and a directed transfer-entropy measure. The method
follows Sackett and others (1979) <doi:10.3758/BF03205679>.

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
