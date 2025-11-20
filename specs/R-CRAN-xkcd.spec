%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xkcd
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Plotting 'ggplot2' Graphics in an 'XKCD' Style

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-stats 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-extrafont 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-Hmisc 
Requires:         R-stats 
Requires:         R-grid 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-extrafont 

%description
Provides custom geoms and themes to create charts and graphics in the
distinctive, hand-drawn 'XKCD' webcomic style using the 'ggplot2'
framework. The package utilizes custom layers for jittered lines,
segments, circles, and figures, and includes a theme that supports the
necessary 'XKCD' font.

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
