%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plot4fun
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Just Plot for Fun

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-pcutils 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-gifski 
BuildRequires:    R-CRAN-showtext 
BuildRequires:    R-CRAN-sysfonts 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-reshape2 
Requires:         R-graphics 
Requires:         R-CRAN-pcutils 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-gifski 
Requires:         R-CRAN-showtext 
Requires:         R-CRAN-sysfonts 

%description
Explore the world of R graphics with fun and interesting plot functions!
Use make_LED() to create dynamic LED screens, draw interconnected rings
with Olympic_rings(), and make festive Chinese couplets with chunlian().
Unleash your creativity and turn data into exciting visuals!

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
