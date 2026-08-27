%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggnext
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Next-Generation Grammar of Graphics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-S7 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
An implementation of the Grammar of Graphics described by Wilkinson (2005,
ISBN:978-0-387-24544-7), built on 'S7' classes. The familiar grammar
vocabulary of aesthetics, geometries, statistics, scales, coordinates,
facets and themes composed with '+' is preserved; every constructor that
takes an argument also accepts a plot as the first argument of a native
pipe ('|>') stage, so the two styles are interchangeable. The package is
extended with built-in interactivity, animation, an exact-data export, a
plot linter that flags common statistical-graphics mistakes before a
figure ships, and a catalogue covering layout diagrams (Sankey, treemap,
network, radar), machine-learning diagnostics (SHAP, receiver operating
characteristic, calibration, partial dependence) and clinical reporting
(Kaplan-Meier, forest, swimmer, CONSORT). Static output is written to
Scalable Vector Graphics; interactive output is a self-contained 'HTML'
document using a canvas element and vanilla 'JavaScript'. Both render
targets consume the same computed-geometry buffer, giving a single source
of truth for layer geometry. Layout and estimation algorithms follow their
published descriptions, including Bruls, Huizing and van Wijk (2000)
<doi:10.1007/978-3-7091-6783-0_4> for squarified treemaps, Fruchterman and
Reingold (1991) <doi:10.1002/spe.4380211102> for force-directed graphs,
and Kaplan and Meier (1958) <doi:10.1080/01621459.1958.10501452> for
survival curves.

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
