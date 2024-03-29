%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PBSmodelling
%global packver   2.69.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.69.3
Release:          1%{?dist}%{?buildtag}
Summary:          GUI Tools Made Easy: Interact with Models and Explore Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
Recommends:       bwidget
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-XML 
Requires:         R-methods 
Requires:         R-tcltk 
Requires:         R-CRAN-XML 

%description
Provides software to facilitate the design, testing, and operation of
computer models. It focuses particularly on tools that make it easy to
construct and edit a customized graphical user interface ('GUI'). Although
our simplified 'GUI' language depends heavily on the R interface to the
'Tcl/Tk' package, a user does not need to know 'Tcl/Tk'. Examples
illustrate models built with other R packages, including 'PBSmapping',
'PBSddesolve', and 'BRugs'. A complete user's guide 'PBSmodelling-UG.pdf'
shows how to use this package effectively.

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
