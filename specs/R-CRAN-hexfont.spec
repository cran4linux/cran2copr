%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hexfont
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          'GNU Unifont' Hex Fonts

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bittermelon >= 1.1.0
BuildRequires:    R-utils 
Requires:         R-CRAN-bittermelon >= 1.1.0
Requires:         R-utils 

%description
Contains all the hex font files from the 'GNU Unifont Project'
<https://unifoundry.com/unifont/> compressed by 'xz'.  'GNU Unifont' is a
duospaced bitmap font that attempts to cover all the official Unicode
glyphs plus several of the artificial scripts in the '(Under-)ConScript
Unicode Registry' <http://www.kreativekorp.com/ucsur/>.  Provides a
convenience function for loading in several of them at the same time as a
'bittermelon' bitmap font object for easy rendering of the glyphs in an
'R' terminal or graphics device.

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
