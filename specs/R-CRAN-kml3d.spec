%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kml3d
%global packver   2.4.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          K-Means for Joint Longitudinal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-longitudinalData >= 2.4.2
BuildRequires:    R-CRAN-kml >= 2.4.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-clv 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-misc3d 
Requires:         R-CRAN-longitudinalData >= 2.4.2
Requires:         R-CRAN-kml >= 2.4.1
Requires:         R-methods 
Requires:         R-CRAN-clv 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-misc3d 

%description
An implementation of k-means specifically design to cluster joint
trajectories (longitudinal data on several variable-trajectories). Like
'kml', it provides facilities to deal with missing value, compute several
quality criterion (Calinski and Harabatz, Ray and Turie, Davies and
Bouldin, BIC,...) and propose a graphical interface for choosing the
'best' number of clusters. In addition, the 3D graph representing the mean
joint-trajectories of each cluster can be exported through LaTeX in a 3D
dynamic rotating PDF graph.

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
