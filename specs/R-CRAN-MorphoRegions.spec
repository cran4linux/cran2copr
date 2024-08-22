%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MorphoRegions
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Regionalization Patterns in Serially Homologous Structures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-cluster >= 2.1.4
BuildRequires:    R-CRAN-pbapply >= 1.7.2
BuildRequires:    R-CRAN-scales >= 1.3.0
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.3
BuildRequires:    R-CRAN-chk >= 0.9.0
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-cluster >= 2.1.4
Requires:         R-CRAN-pbapply >= 1.7.2
Requires:         R-CRAN-scales >= 1.3.0
Requires:         R-CRAN-RColorBrewer >= 1.1.3
Requires:         R-CRAN-chk >= 0.9.0
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Computes the optimal number of regions (or subdivisions) and their
position in serial structures without a priori assumptions and to
visualize the results. After reducing data dimensionality with the
built-in function for data ordination, regions are fitted as segmented
linear regressions along the serial structure. Every region boundary
position and increasing number of regions are iteratively fitted and the
best model (number of regions and boundary positions) is selected with an
information criterion. This package expands on the previous 'regions'
package (Jones et al., Science 2018) with improved computation and more
fitting and plotting options.

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
