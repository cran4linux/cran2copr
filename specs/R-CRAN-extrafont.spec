%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  extrafont
%global packver   0.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.19
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Using Fonts

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-CRAN-extrafontdb 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rttf2pt1 
Requires:         R-CRAN-extrafontdb 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-Rttf2pt1 

%description
Tools to using fonts other than the standard PostScript fonts. This
package makes it easy to use system TrueType fonts and with PDF or
PostScript output files, and with bitmap output files in Windows.
extrafont can also be used with fonts packaged specifically to be used
with, such as the fontcm package, which has Computer Modern PostScript
fonts with math symbols.

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
