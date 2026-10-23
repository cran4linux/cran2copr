%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  umg
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Unified Model Graphs for Statistical Models in Psychology

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Constructs, validates, lays out, and renders Unified Model Graphs (UMG), a
formal graphical grammar for statistical models in psychology. Vertices
are typed by observability, support, and inferential role; edges
distinguish stochastic, symmetric, deterministic, and mixing dependence;
plates encode replication and hierarchy. Diagrams can be themed and
rendered with base 'grid' graphics, with 'ggplot2', as 'TikZ' code, or as
'Graphviz' DOT, and can be constructed either from one-line motif builders
for many model families or automatically from 'lavaan', 'lme4', 'mirt',
'blavaan', 'brms', 'OpenMx', and 'qgraph' model objects. A diagram can be
inspected as a data frame, summarised, and exported back to 'lavaan' model
syntax, making the model-diagram correspondence operational in both
directions. Each diagram also exposes identification diagnostics (scaling
checks, a graphical counting rule, and a d-separation reader) and
generates the exploratory display scaffolds implied by the model-data
duality. The notation builds on established results for graphical and
structural equation models: plate notation follows Buntine (1994)
<doi:10.1613/jair.62>; the counting rule and scaling checks follow Bollen
(1989) <doi:10.1002/9781118619179>; and the independence reader implements
the d-separation criterion of Geiger, Verma and Pearl (1990)
<doi:10.1002/net.3230200504> through the equivalent ancestral graph
criterion of Lauritzen, Dawid, Larsen and Leimer (1990)
<doi:10.1002/net.3230200503>.

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
