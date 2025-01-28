%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  somhca
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Self-Organising Maps Coupled with Hierarchical Cluster Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-kohonen 
BuildRequires:    R-CRAN-aweSOM 
BuildRequires:    R-CRAN-maptree 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-kohonen 
Requires:         R-CRAN-aweSOM 
Requires:         R-CRAN-maptree 
Requires:         R-CRAN-RColorBrewer 

%description
Implements self-organising maps combined with hierarchical cluster
analysis (SOM-HCA) for clustering and visualization of high-dimensional
data. The package includes functions to estimate the optimal map size
based on various quality measures and to generate a model using the
selected dimensions. It also performs hierarchical clustering on the map
nodes to group similar units. Documentation about the SOM-HCA method is
provided in Pastorelli et al. (2024) <doi:10.1002/xrs.3388>.

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
