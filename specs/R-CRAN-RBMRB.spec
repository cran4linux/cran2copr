%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RBMRB
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the Biological Magnetic Resonance Data Bank ('BMRB')

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.10.0
BuildRequires:    R-CRAN-cli >= 3.4.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-plotly >= 4.10.0
Requires:         R-CRAN-cli >= 3.4.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-httr2 >= 1.0.0

%description
A comprehensive interface to the Biological Magnetic Resonance Data Bank
('BMRB') <https://bmrb.io>, mirroring all functionality of the 'PyBMRB'
'Python' package (v3.0). Provides four modules: (1) 'ChemicalShift' for
fetching per-entry chemical shift data from the 'BMRB' 'REST' 'API' or
local 'NMR-STAR' files; (2) 'ChemicalShiftStatistics' for database-wide
statistical queries; (3) Spectra for simulating '1H-15N' 'HSQC', '1H-13C'
'HSQC', '1H-1H' 'TOCSY', and generic 2D 'NMR' spectra as interactive
plots; and (4) Histogram for chemical shift distribution visualizations
with optional filtering by pH, temperature, and ambiguity code. All
interactive plots are rendered via 'plotly'. Uses the 'BMRB' REST API v2
<https://api.bmrb.io/v2/>.

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
