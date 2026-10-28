%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  transformerpalettes
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Color Palettes Inspired by Transformers Toys, Cartoons and Comics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Color palettes drawn from the Transformers franchise, centered on the
1984-1989 Generation 1 toys and extending to their Generation 2
re-releases, the cartoon animation models and the Marvel comics. Covers
the leaders, every member and combined form of the combiner teams
(Aerialbots, Protectobots, Technobots, Constructicons, Stunticons,
Combaticons, Terrorcons, Predacons, Seacons, Pretender Monsters and
Breastforce), the Dinobots, the Seeker jets, Soundwave and the cassettes,
the Insecticons, the 1984 Autobot cars and Mini Vehicles and the 1986
movie cast, with separate palettes for the toy, the cartoon animation
model, the Marvel comic coloring and the Generation 2 re-release where
each exists. Includes 'ggplot2' color and fill scales for discrete and
continuous data, team palettes that take one color from each member of a
combiner team, metadata linking each palette to its character, faction,
team and reference page, and helpers to shortlist palettes that suit
categorical, color-blind-safe, sequential or diverging use. Hex values are
approximations of the toys' plastic and paint colors; the package is a fan
project and is not affiliated with or endorsed by Hasbro or Takara Tomy.

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
