%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gpbiometrics
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Process and Report Gazepoint Biometrics Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Gazepoint-native tools for reproducible analysis and reporting of
Gazepoint Biometrics and GP3-derived physiological, gaze, pupil, fixation,
AOI, marker, and event-level exports. The package supports import,
validation, preprocessing, missing-value imputation, EDA/GSR, SCR
epoching, IBI/RR/HRV, PPG/pulse workflows, pupil blink detection and
cleaning, gaze filtering, fixation summaries, engagement-dial indices,
multimodal trial regressors, quality reports, exclusion and QC
recommendations, synthetic eye-data generation, and interoperability or
workflow-inspired helpers for common psychophysiology toolchains. The
package is designed for transparent, CRAN-safe, scriptable analysis rather
than as a full clone of external commercial or open-source toolboxes.

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
