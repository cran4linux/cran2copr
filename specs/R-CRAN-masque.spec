%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  masque
%global packver   0.16.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.0
Release:          1%{?dist}%{?buildtag}
Summary:          Structurally Faithful Development Surrogates for Tabular Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-S7 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Turns a confidential tabular dataset - a single table, a folder of files,
or a multi-sheet workbook - into a structurally faithful synthetic clone
suitable for pipeline development. Experimental-design allocation and the
NA pattern are preserved exactly; categorical design, treatment, and
covariate vocabularies can be reversibly aliased; outcome and
numeric-covariate values are re-simulated via a Gaussian copula that
preserves the global covariance structure. Columns shared across tables
are aliased consistently so the synthetic tables still join. A private
recipe object round-trips a pipeline written against the synthetic clone
onto the original data. Not a differential-privacy or anonymisation tool:
outputs are development surrogates, not public-release-safe artefacts.

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
