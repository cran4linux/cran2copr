%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MG1StationaryProbability
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Computes Stationary Distribution for M/G/1 Queuing System

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-memoise >= 2.0.1
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-doParallel >= 1.0.17
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-memoise >= 2.0.1
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-doParallel >= 1.0.17
Requires:         R-parallel 
Requires:         R-stats 

%description
The idea of a computational algorithm described in the article by Andronov
M. et al. (2022)
<https://link.springer.com/chapter/10.1007/978-3-030-92507-9_13>. The
purpose of this package is to automate computations for a Markov-Modulated
M/G/1 queuing system with alternating Poisson flow of arrivals. It offers
a set of functions to calculate various mean indices of the system,
including mean flow intensity, mean service busy and idle times, and the
system's stationary probability.

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
