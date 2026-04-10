%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  palimpsestr
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          1%{?dist}%{?buildtag}
Summary:          Probabilistic Decomposition of Archaeological Palimpsests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Probabilistic framework for the analysis of archaeological palimpsests
based on the Stratigraphic Entanglement Field (SEF). Integrates spatial
proximity, stratigraphic depth, chronological overlap, and cultural
similarity to estimate latent depositional phases via diagonal Gaussian
mixture Expectation-Maximisation (EM). Provides the Stratigraphic
Entanglement Index (SEI), Excavation Stratigraphic Energy (ESE), and
Palimpsest Dissolution Index (PDI) for quantifying depositional coherence,
detecting intrusive finds, and measuring palimpsest formation. Includes
simulation, diagnostics, phase-count selection, publication-quality plots,
and Geographic Information System (GIS) export via 'sf'. Methods are
described in Cocca (2026) <https://github.com/enzococca/palimpsestr>.

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
