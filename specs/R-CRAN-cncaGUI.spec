%global __brp_check_rpaths %{nil}
%global packname  cncaGUI
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Canonical Non-Symmetrical Correspondence Analysis in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
Requires:         tcl
Requires:         tk
Requires:         bwidget
BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-shapes 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-tkrplot 
Requires:         R-tcltk 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-shapes 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-MASS 

%description
A GUI with which users can construct and interact with Canonical
Correspondence Analysis and Canonical Non-Symmetrical Correspondence
Analysis and provides inferential results by using Bootstrap Methods.

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
