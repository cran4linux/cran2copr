%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  traj
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Trajectory Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-NbClust 
BuildRequires:    R-CRAN-pastecs 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cluster 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-NbClust 
Requires:         R-CRAN-pastecs 
Requires:         R-CRAN-psych 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements the three-step procedure proposed by Leffondree et al. (2004)
to identify clusters of individual longitudinal trajectories. The
procedure involves (1) calculating 24 measures describing the features of
the trajectories; (2) using factor analysis to select a subset of the 24
measures and (3) using cluster analysis to identify clusters of
trajectories, and classify each individual trajectory in one of the
clusters.

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
