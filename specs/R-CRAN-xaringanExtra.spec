%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xaringanExtra
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extras and Extensions for 'xaringan' Slides

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-knitr 
Requires:         R-utils 
Requires:         R-CRAN-uuid 

%description
Extras and extensions for 'xaringan' slides. Navigate your slides with
tile view. Make your slides editable, live! Announce slide changes with
subtle tones. Animate slide transitions with 'animate.css'. Add tabbed
panels to slides with 'panelset'. Use the 'Tachyons CSS' utility toolkit
for rapid slide development. Scribble on your slides. Add a copy button to
your code chunks with 'clipboard'. Add a logo or top or bottom banner to
every slide. Broadcast slides to stay in sync with remote viewers. Include
yourself in your slides with 'webcam'.  Plus a whole lot more!

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
