%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ddc
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Distance Density Clustering Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dtwclust >= 5.5
BuildRequires:    R-parallel >= 4.2
BuildRequires:    R-CRAN-magrittr >= 2.0
BuildRequires:    R-CRAN-dtw >= 1.22
BuildRequires:    R-utils 
Requires:         R-CRAN-dtwclust >= 5.5
Requires:         R-parallel >= 4.2
Requires:         R-CRAN-magrittr >= 2.0
Requires:         R-CRAN-dtw >= 1.22
Requires:         R-utils 

%description
A distance density clustering (DDC) algorithm in R. DDC uses dynamic time
warping (DTW) to compute a similarity matrix, based on which cluster
centers and cluster assignments are found. DDC inherits dynamic time
warping (DTW) arguments and constraints. The cluster centers are centroid
points that are calculated using the DTW Barycenter Averaging (DBA)
algorithm. The clustering process is divisive. At each iteration, cluster
centers are updated and data is reassigned to cluster centers. Early
stopping is possible. The output includes cluster centers and clustering
assignment, as described in the paper (Ma et al (2017)
<doi:10.1109/ICDMW.2017.11>).

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
