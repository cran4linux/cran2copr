%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcmdrPlugin.KMggplot2
%global packver   0.2-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          R Commander Plug-in for Data Visualization with 'ggplot2'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggthemes >= 5.0.0
BuildRequires:    R-CRAN-survival >= 3.4.0.1
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-Rcmdr >= 2.6.0
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-scales >= 1.3.0
BuildRequires:    R-CRAN-tcltk2 >= 1.2.11
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.3
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggthemes >= 5.0.0
Requires:         R-CRAN-survival >= 3.4.0.1
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-Rcmdr >= 2.6.0
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-scales >= 1.3.0
Requires:         R-CRAN-tcltk2 >= 1.2.11
Requires:         R-CRAN-RColorBrewer >= 1.1.3
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-rlang 

%description
A GUI front-end for 'ggplot2' supports Kaplan-Meier plot, histogram, Q-Q
plot, box plot, errorbar plot, scatter plot, line chart, pie chart, bar
chart, contour plot, and distribution plot.

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
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
