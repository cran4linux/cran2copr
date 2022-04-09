%global __brp_check_rpaths %{nil}
%global packname  TippingPoint
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Enhanced Tipping Point Displays the Results of Sensitivity Analysis for Missing Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-reshape2 

%description
Using the idea of "tipping point" (proposed in Gregory Campbell, Gene
Pennello and Lilly Yue(2011) <DOI:10.1080/10543406.2011.550094>) to
visualize the results of sensitivity analysis for missing data, the
package provides a set of functions to list out all the possible
combinations of missing values in two treatment arms, calculate
corresponding estimated treatment effects and p values, and draw a colored
heat-map. It could deal with randomized experiments with a binary outcome
or a continuous outcome. In addition, the package provides a visualized
method to compare various imputation methods by adding the rectangles or
convex hulls on the basic plot.

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
