%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FKmL
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fréchet Distance-Based K-Means and Extensions for Longitudinal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-abind 

%description
Implements shape-based clustering algorithms for multidimensional
longitudinal data based on the Fréchet distance. It implements two main
methods: MFKmL (Multidimensional Fréchet distance-based K-means for
Longitudinal data), an extension of the K-means algorithm using the
Fréchet distance originally developed in the 'kmlShape' package, adapted
for multidimensional trajectories; and SFKmL (Sparse multidimensional
Fréchet distance-based K-medoids for Longitudinal data), a K-medoids-based
clustering algorithm that incorporates variable selection. These tools are
designed to enhance clustering performance in high-dimensional
longitudinal data settings, particularly those with time delays,
variations in trajectory speed, irregular sampling intervals, and noise.
This package implements methods derived from Kang et al. (2023)
<doi:10.1007/s11222-023-10237-z>.

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
