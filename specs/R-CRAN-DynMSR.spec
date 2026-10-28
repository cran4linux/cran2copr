%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DynMSR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Connect Systems Biology and Pharmacology Formats to Simulation Backends

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-jsonvalidate 
BuildRequires:    R-CRAN-whisker 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-jsonvalidate 
Requires:         R-CRAN-whisker 

%description
Provides a convenient R interface for systems-biology and
systems-pharmacology models in Heta, SBML (Systems Biology Markup
Language), and DynMS (Dynamic Model Specification) formats. DynMS JSON
files are loaded directly; Heta projects and SBML files are converted to
DynMS by an optional compatible installation of 'heta-compiler'. Models
can be validated, selected from a platform, and generated or built for
simulation with 'mrgsolve' as a backend.

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
