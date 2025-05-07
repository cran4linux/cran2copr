%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gauseR
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Lotka-Volterra Models for Gause's 'Struggle for Existence'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-deSolve 
Requires:         R-stats 
Requires:         R-graphics 

%description
A collection of tools and data for analyzing the Gause microcosm
experiments, and for fitting Lotka-Volterra models to time series data.
Includes methods for fitting single-species logistic growth, and
multi-species interaction models, e.g. of competition, predator/prey
relationships, or mutualism. See documentation for individual functions
for examples. In general, see the lv_optim() function for examples of how
to fit parameter values in multi-species systems. Note that the general
methods applied here, as well as the form of the differential equations
that we use, are described in detail in the Quantitative Ecology textbook
by Lehman et al., available at <http://hdl.handle.net/11299/204551>, and
in Lina K. Mühlbauer, Maximilienne Schulze, W. Stanley Harpole, and Adam
T. Clark. 'gauseR': Simple methods for fitting Lotka-Volterra models
describing Gause's 'Struggle for Existence' in the journal Ecology and
Evolution.

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
