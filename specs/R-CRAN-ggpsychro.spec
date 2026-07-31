%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggpsychro
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Psychrometric Charts

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-gridGeometry 
BuildRequires:    R-CRAN-polyclip 
BuildRequires:    R-CRAN-isoband 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-psychrolib 
BuildRequires:    R-CRAN-S7 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-gridGeometry 
Requires:         R-CRAN-polyclip 
Requires:         R-CRAN-isoband 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-psychrolib 
Requires:         R-CRAN-S7 

%description
Provides 'ggplot2' coordinates, layers, scales, themes, and presets for
creating psychrometric charts. The package supports metric and inch-pound
unit systems, psychrometric grids, state points, process lines, zones, and
thermal comfort overlays for heating, ventilation, air conditioning, and
building performance workflows. Psychrometric property calculations are
based on 'PsychroLib' (Meyer and Thevenard, 2019)
<doi:10.21105/joss.01137> where appropriate.

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
