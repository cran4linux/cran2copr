%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bgbcalc
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculations for German Civil Code Rules ('BGB-Rechenregeln')

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-utils 
Requires:         R-stats 

%description
Numerical and calendar calculations for provisions of the German Civil
Code ('Buergerliches Gesetzbuch', BGB)
<https://www.gesetze-im-internet.de/bgb/>. Covers time limits ('Fristen'),
interest ('Zinsen'), monetary limits ('Betragsgrenzen'), proportional
allocations ('Quoten') and inheritance calculations ('Erbrecht'). German
parameter names preserve statutory terminology ('deutsche
Rechtsbegriffe'). Results include exact fractions ('Brueche'), calculation
steps ('Rechenschritte'), assumptions ('Annahmen') and a fixed source
identifier ('Quellenfassung'). Legal conditions require qualified inputs.
Conditional models require justified method choices ('Methodenwahl');
universal legal completeness is not asserted ('keine umfassende
Rechtsentscheidung').

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
