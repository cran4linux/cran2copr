%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  orbis
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive and High-Resolution Layered Graphics with Built-in World Maps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-htmltools 

%description
A layered grammar of graphics that compiles plots to a
resolution-independent scene description and renders it through two
back-ends: a self-contained SVG writer with embedded 'JavaScript' for
interactive figures (tooltips, hover highlighting, zoom, pan and legend
toggling) and R's own graphics devices for publication-quality output at
any resolution. Geographic layers are first class: a simplified world
polygon dataset ships with the package and can be drawn with several map
projections, including Robinson, Equal Earth and an orthographic globe.
The layered grammar follows Wickham (2010) <doi:10.1198/jcgs.2009.07098>;
projections follow Snyder (1987) <doi:10.3133/pp1395> and, for Equal
Earth, Savric, Patterson and Jenny (2019)
<doi:10.1080/13658816.2018.1504949>; line simplification uses Douglas and
Peucker (1973) <doi:10.3138/FM57-6770-U75U-7727>; the default colour
scales follow the guidance on perceptually uniform palettes of Crameri,
Shephard and Heron (2020) <doi:10.1038/s41467-020-19160-7>.

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
