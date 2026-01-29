%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  traj
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Feature-Based Clustering of Longitudinal Trajectories

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-clusterCrit 
BuildRequires:    R-CRAN-fclust 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-e1071 
Requires:         R-stats 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-clusterCrit 
Requires:         R-CRAN-fclust 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-e1071 

%description
Identifies clusters of individual longitudinal trajectories. In the spirit
of Leffondre et al. (2004), the procedure involves identifying each
trajectory to a point in the space of measures. In this context, a measure
is a quantity meant to capture a certain characteristic feature of the
trajectory. The points in the space of measures are then clustered using a
version of spectral clustering.

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
