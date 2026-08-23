%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  colorr
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Color Palettes for Soccer, MLB, NBA, WNBA, NHL, and NFL Teams

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-grDevices 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-grDevices 

%description
Current-season color palettes for soccer clubs in the English Premier
League ('EPL'), 'LaLiga', 'Serie A', the 'Bundesliga', 'Ligue 1' and Major
League Soccer ('MLS'), and for Major League Baseball ('MLB'), National
Basketball Association ('NBA'), Women's National Basketball Association
('WNBA'), National Hockey League ('NHL') and National Football League
('NFL') teams. Palettes are returned as named character vectors of hex
colors, and as 'ggplot2' colour and fill scales. The palettes shipped in
earlier versions of the package remain available so that older figures
stay reproducible.

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
