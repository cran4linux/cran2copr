%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  colourspace
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Convert from One Colour Space to Another, Print a Ready-to-Paste Modern 'CSS' Syntax

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-farver 
BuildRequires:    R-CRAN-RANN 
Requires:         R-CRAN-farver 
Requires:         R-CRAN-RANN 

%description
Provides a comprehensive 'API' for colour conversion between popular
colour spaces ('RGB', 'HSL', 'OKLab', 'OKLch', 'hex', and named colours)
along with clean, modern 'CSS' Color Level 4 syntax output. Integrates
seamlessly into 'Shiny' and 'Quarto' workflows. Includes nearest colour
name lookup powered by a curated database of over 30,000 colour names.
'OKLab'/'OKLCh' colour spaces are described in Ottosson (2020)
<https://bottosson.github.io/posts/oklab/>. 'CSS' Color Level 4 syntax
follows the W3C specification <https://www.w3.org/TR/css-color-4/>.

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
