%global packname  loon.shiny
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automatically Create a 'Shiny' App Based on Interactive 'Loon' Widgets

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-loon >= 1.3.0
BuildRequires:    R-CRAN-loon.ggplot >= 1.1.0
BuildRequires:    R-tcltk 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-loon >= 1.3.0
Requires:         R-CRAN-loon.ggplot >= 1.1.0
Requires:         R-tcltk 
Requires:         R-methods 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-base64enc 

%description
Package 'shiny' provides interactive web applications in R. Package 'loon'
is an interactive toolkit engaged in open-ended, creative and unscripted
data exploration. The 'loon.shiny' package can take 'loon' widgets and
display a selfsame 'shiny' app.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
