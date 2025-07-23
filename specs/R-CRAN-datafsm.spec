%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  datafsm
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Finite State Machine Models from Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-caret >= 6.0
BuildRequires:    R-methods >= 4.0
BuildRequires:    R-stats >= 4.0
BuildRequires:    R-CRAN-GA >= 3.2
BuildRequires:    R-CRAN-Rcpp >= 1.0
Requires:         R-CRAN-caret >= 6.0
Requires:         R-methods >= 4.0
Requires:         R-stats >= 4.0
Requires:         R-CRAN-GA >= 3.2
Requires:         R-CRAN-Rcpp >= 1.0

%description
Automatic generation of finite state machine models of dynamic
decision-making that both have strong predictive power and are
interpretable in human terms. We use an efficient model representation and
a genetic algorithm-based estimation process to generate simple
deterministic approximations that explain most of the structure of complex
stochastic processes. We have applied the software to empirical data, and
demonstrated it's ability to recover known data-generating processes by
simulating data with agent-based models and correctly deriving the
underlying decision models for multiple agent models and degrees of
stochasticity.

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
