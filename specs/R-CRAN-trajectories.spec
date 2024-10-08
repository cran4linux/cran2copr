%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  trajectories
%global packver   0.2-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.9
Release:          1%{?dist}%{?buildtag}
Summary:          Classes and Methods for Trajectory Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp >= 1.1.0
BuildRequires:    R-CRAN-spacetime >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-sp >= 1.1.0
Requires:         R-CRAN-spacetime >= 1.0.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-zoo 

%description
Classes and methods for trajectory data, with support for nesting
individual Track objects in track sets (Tracks) and track sets for
different entities in collections of Tracks. Methods include selection,
generalization, aggregation, intersection, simulation, and plotting.

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
