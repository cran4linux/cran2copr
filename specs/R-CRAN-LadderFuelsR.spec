%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LadderFuelsR
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Tool for Vertical Fuel Continuity Analysis using Airborne Laser Scanning Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-segmented 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-segmented 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 

%description
Set of tools for analyzing vertical fuel continuity at the tree level
using Airborne Laser Scanning data. The workflow consisted of: 1)
calculating the vertical height profiles of each segmented tree; 2)
identifying gaps and fuel layers; 3) estimating the distance between fuel
layers; and 4) retrieving the fuel layers base height and depth.
Additionally, other functions recalculate previous metrics after
considering distances greater than 1 m and calculate the canopy base
height as the fuel base height located at the largest- and at the
last-distance. Moreover, the package calculates: i) the percentage of Leaf
Area Density comprised in each fuel layer, ii) remove fuel layers with
Leaf Area Density percentage less than 25, iii) recalculate the distances
among the reminder ones, and iv) identify the canopy base height as the
fuel base height with the highest Leaf Area Density percentage. On the
other hand, when there is only one fuel layer, it identifies the canopy
base height performing a segmented linear regression (breaking points) on
the cumulative sum of Leaf Area Density as a function of height. Finally,
a collection of plotting functions is developed to represent: i) the
initial gaps and fuel layers; ii) the fuels base height, depths and gaps
with distances greater than 1 m and, iii) the fuels base height and depths
after applying the breaking point method over trees with only one fuel
layer. The methods implemented in this package are original and have not
been published elsewhere.

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
