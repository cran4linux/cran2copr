%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BORG
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bounded Outcome Risk Guard for Model Evaluation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Comprehensive toolkit for valid spatial, temporal, and grouped model
evaluation. Automatically detects data dependencies (spatial
autocorrelation, temporal structure, clustered observations), generates
appropriate cross-validation schemes (spatial blocking, checkerboard,
hexagonal, KNNDM, environmental blocking, leave-location-out, purged CV),
and validates evaluation pipelines for leakage. Includes area of
applicability (AOA) assessment following Meyer & Pebesma (2021)
<doi:10.1111/2041-210X.13650>, forward feature selection with blocked CV,
spatial thinning, block-permutation variable importance, extrapolation
detection, and interactive visualizations. Integrates with 'tidymodels',
'caret', 'mlr3', 'ENMeval', and 'biomod2'. Based on evaluation principles
described in Roberts et al. (2017) <doi:10.1111/ecog.02881>, Kaufman et
al. (2012) <doi:10.1145/2382577.2382579>, Kapoor & Narayanan (2023)
<doi:10.1016/j.patter.2023.100804>, and Linnenbrink et al. (2024)
<doi:10.5194/gmd-17-5897-2024>.

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
