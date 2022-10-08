%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RSiena
%global packver   1.3.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.13
Release:          1%{?dist}%{?buildtag}
Summary:          Siena - Simulation Investigation for Empirical Network Analysis

License:          GPL-2 | GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
Requires:         tcl
Requires:         tk
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-lattice 
Requires:         R-parallel 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-xtable 

%description
The main purpose of this package is to perform simulation-based estimation
of stochastic actor-oriented models for longitudinal network data
collected as panel data. Dependent variables can be single or multivariate
networks, which can be directed, non-directed, or two-mode; and associated
actor variables. There are also functions for testing parameters and
checking goodness of fit. An overview of these models is given in Tom A.B.
Snijders (2017), Stochastic Actor-Oriented Models for Network Dynamics,
Annual Review of Statistics and Its Application, 4, 343-363 <doi:
10.1146/annurev-statistics-060116-054035>. An extensive manual, scripts,
and much further information is at the Siena website
<http://www.stats.ox.ac.uk/~snijders/siena/>.

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
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
