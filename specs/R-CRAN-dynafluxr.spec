%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dynafluxr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieve Reaction Rate Dynamics from Metabolite Concentration Time Courses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bspline >= 2.5.0
BuildRequires:    R-CRAN-nlsic >= 1.1.1
BuildRequires:    R-CRAN-gmresls >= 0.2
BuildRequires:    R-CRAN-optparse 
BuildRequires:    R-CRAN-qpdf 
BuildRequires:    R-CRAN-arrApply 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyFiles 
Requires:         R-CRAN-bspline >= 2.5.0
Requires:         R-CRAN-nlsic >= 1.1.1
Requires:         R-CRAN-gmresls >= 0.2
Requires:         R-CRAN-optparse 
Requires:         R-CRAN-qpdf 
Requires:         R-CRAN-arrApply 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyFiles 

%description
Reaction rate dynamics can be retrieved from metabolite concentration time
courses. User has to provide corresponding stoichiometric matrix but not a
regulation model (Michaelis-Menten or similar). Instead of solving an
ordinary differential equation (ODE) system describing the evolution of
concentrations, we use B-splines to catch the concentration and rate
dynamics then solve a least square problem on their coefficients with
non-negativity (and optionally monotonicity) constraints. Constraints can
be also set on initial values of concentration. The package 'dynafluxr'
can be used as a library but also as an application with command line
interface dynafluxr::cli("-h") or graphical user interface
dynafluxr::gui().

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
