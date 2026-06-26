%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ratecalib
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calibration Weighting to Multiple Subgroup Pass-Rate Targets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-osqp 
Requires:         R-stats 

%description
Calibration weighting for binary-outcome pass rates against multiple
overlapping subgroup targets. Adjusts initial positive weights so that the
overall pass rate and subgroup pass rates approach (soft mode) or exactly
match (exact mode) given targets, while preserving the initial weight
structure and population margins. Provides a one-step interface, pre-solve
data checks, target-table construction, effective sample size and
design-effect diagnostics, and example data. The solver works on a bounded
convex quadratic program over demographic-cell-by-outcome aggregates for
efficiency on large samples. Methods follow the calibration approach of
Deville and Saerndal (1992) <doi:10.1080/01621459.1992.10475217>.

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
