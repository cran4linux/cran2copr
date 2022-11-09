%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FFD
%global packver   1.0-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Freedom from Disease

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
Requires:         bwidget
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-R2HTML 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-tcltk 
Requires:         R-CRAN-R2HTML 

%description
Functions, S4 classes/methods and a graphical user interface (GUI) to
design surveys to substantiate freedom from disease using a modified
hypergeometric function (see Cameron and Baldock, 1997,
<doi:10.1016/s0167-5877(97)00081-0>). Herd sensitivities are computed
according to sampling strategies "individual sampling" or "limited
sampling" (see M. Ziller, T. Selhorst, J. Teuffert, M. Kramer and H.
Schlueter, 2002, <doi:10.1016/S0167-5877(01)00245-8>). Methods to compute
the a-posteriori alpha-error are implemented. Risk-based targeted sampling
is supported.

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
