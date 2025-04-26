%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rmoji
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactively Insert Emojis in 'R' Documents

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 

%description
Provides an intuitive and user-friendly interface for working with emojis
in 'R'. It allows users to search, insert, and manage emojis by keyword,
category, or through an interactive 'shiny'-based drop-down. The package
enables integration of emojis into 'R' scripts, 'R Markdown', 'Quarto',
'shiny' apps, and 'ggplot2' plots. Also includes built-in mappings for
commit messages, useful for version control. It builds on established
emoji libraries and Unicode standards, adding expressiveness and visual
cues to documentation, user interfaces, and reports. For more details see
'Emojipedia' (2024) <https://emojipedia.org> and GitHub Emoji Cheat Sheet
<https://github.com/ikatyang/emoji-cheat-sheet/tree/master>.

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
