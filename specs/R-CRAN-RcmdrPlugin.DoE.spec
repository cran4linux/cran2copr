%global __brp_check_rpaths %{nil}
%global packname  RcmdrPlugin.DoE
%global packver   0.12-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.4
Release:          1%{?dist}%{?buildtag}
Summary:          R Commander Plugin for (Industrial) Design of Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FrF2 >= 1.2.10
BuildRequires:    R-CRAN-DoE.wrapper >= 0.8
BuildRequires:    R-CRAN-DoE.base >= 0.22
BuildRequires:    R-utils 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-Rcmdr 
BuildRequires:    R-CRAN-RcmdrMisc 
Requires:         R-CRAN-FrF2 >= 1.2.10
Requires:         R-CRAN-DoE.wrapper >= 0.8
Requires:         R-CRAN-DoE.base >= 0.22
Requires:         R-utils 
Requires:         R-tcltk 
Requires:         R-CRAN-Rcmdr 
Requires:         R-CRAN-RcmdrMisc 

%description
Provides a platform-independent GUI for design of experiments. The package
is implemented as a plugin to the R-Commander, which is a more general
graphical user interface for statistics in R based on tcl/tk. DoE
functionality can be accessed through the menu Design that is added to the
R-Commander menus.

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
