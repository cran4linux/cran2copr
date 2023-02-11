%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sfhotspot
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hot-Spot Analysis with Simple Features

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-SpatialKDE 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-SpatialKDE 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-tibble 

%description
Identify and understand clusters of points (typically representing the
locations of places or events) stored in simple-features (SF) objects.
This is useful for analysing, for example, hot-spots of crime events. The
package emphasises producing results from point SF data in a single step
using reasonable default values for all other arguments, to aid rapid data
analysis by users who are starting out. Functions available include kernel
density estimation (for details, see Yip (2020)
<doi:10.22224/gistbok/2020.1.12>), analysis of spatial association (Getis
and Ord (1992) <doi:10.1111/j.1538-4632.1992.tb00261.x>) and hot-spot
classification (Chainey (2020) ISBN:158948584X).

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
