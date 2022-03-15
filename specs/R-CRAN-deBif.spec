%global __brp_check_rpaths %{nil}
%global packname  deBif
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bifurcation Analysis of Ordinary Differential Equation Systems

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-shinyjs >= 2.0
BuildRequires:    R-CRAN-shinydashboardPlus >= 2.0
BuildRequires:    R-CRAN-rootSolve >= 1.8
BuildRequires:    R-CRAN-shiny >= 1.7
BuildRequires:    R-CRAN-deSolve >= 1.3
BuildRequires:    R-CRAN-shinydashboard >= 0.7
BuildRequires:    R-CRAN-rstudioapi >= 0.13
BuildRequires:    R-graphics 
Requires:         R-CRAN-shinyjs >= 2.0
Requires:         R-CRAN-shinydashboardPlus >= 2.0
Requires:         R-CRAN-rootSolve >= 1.8
Requires:         R-CRAN-shiny >= 1.7
Requires:         R-CRAN-deSolve >= 1.3
Requires:         R-CRAN-shinydashboard >= 0.7
Requires:         R-CRAN-rstudioapi >= 0.13
Requires:         R-graphics 

%description
Shiny application that performs bifurcation and phaseplane analysis of
systems of ordinary differential equations. The package allows for
computation of equilibrium curves as a function of a single free
parameter, detection of transcritical, saddle-node and hopf bifurcation
points along these curves, and computation of curves representing these
transcritical, saddle-node and hopf bifurcation points as a function of
two free parameters. The shiny-based GUI allows visualization of the
results in both 2D- and 3D-plots. The implemented methods for solution
localisation and curve continuation are based on the book "Elements of
applied bifurcation theory" (Kuznetsov, Y. A., 1995; ISBN: 0-387-94418-4).

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
