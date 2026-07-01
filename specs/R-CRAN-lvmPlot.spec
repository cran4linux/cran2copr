%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lvmPlot
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Publication-Quality Diagrams for Latent Variable Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Converts output from latent variable model tools into publication-ready
path diagrams and model schematics. 'lavaan' fit objects and parameter
tables are supported as a primary workflow, with graph adapters for
objects from 'blavaan', 'lavaan.mi', 'semPlot', 'mirt', 'eRm', 'OpenMx',
'psych', 'poLCA', 'mclust', 'flexmix', 'lcmm', 'tidyLPA', and
'MplusAutomation' workflows when those packages are available. Supports
structural equation and confirmatory factor analysis diagrams, multilevel
structural equation models, growth models, higher-order factor models,
latent class and profile models, item response theory models, and common
mixture outputs through a unified graph grammar with model-aware defaults,
geometry diagnostics, layout quality scoring, automatic layout selection,
customizable publication styles, 'RStudio' preview, SVG/PDF/PNG export,
'TikZ' output, and reproducible publication bundles.

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
