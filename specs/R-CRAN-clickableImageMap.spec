%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clickableImageMap
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Implement 'tableGrob' Object as a Clickable Image Map

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplotify 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplotify 
Requires:         R-grid 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-gtable 
Requires:         R-grDevices 

%description
Implement 'tableGrob' object as a clickable image map. The
'clickableImageMap' package is designed to be more convenient and more
configurable than the edit() function. Limitations that I have encountered
with edit() are cannot control (1) positioning (2) size (3) appearance and
formatting of fonts In contrast, when the table is implemented as a
'tableGrob', all of these features are controllable. In particular, the
'ggplot2' grid system allows exact positioning of the table relative to
other graphics etc.

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
