%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  actiRhythm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Circadian Rest-Activity Rhythm Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-DBI 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-scales 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-utils 

%description
Quantifies the circadian rest-activity rhythm, the roughly 24-hour cycle
of activity and rest, from activity counts and raw accelerometer
recordings. Analyses run on an activity-count vector and its timestamps,
and a built-in reader loads 'ActiGraph' '.agd' files (an 'SQLite'
database) directly. Computes nonparametric metrics (interdaily stability
(IS) and intradaily variability (IV) following Witting et al. (1990)
<doi:10.1016/0006-3223(90)90523-5>; relative amplitude (RA), the
least-active 5-hour window (L5), and the most-active 10-hour window (M10)
following Van Someren et al. (1999) <doi:10.3109/07420529908998724>),
cosinor models with a rhythmicity test, confidence ellipses,
population-mean cosinor, and two-group parameter comparison (Cornelissen
(2014) <doi:10.1186/1742-4682-11-16>; Marler et al. (2006)
<doi:10.1002/sim.2466>), period estimation by Lomb-Scargle (Lomb (1976)
<doi:10.1007/BF00648343>; Scargle (1982) <doi:10.1086/160554>) and
chi-square (Sokolove and Bushell (1978)
<doi:10.1016/0022-5193(78)90022-X>) periodograms with bootstrap confidence
intervals and a sliding-window spectrogram, fractal and nonlinear measures
(Peng et al. (1994) <doi:10.1103/PhysRevE.49.1685>; Kantelhardt et al.
(2002) <doi:10.1016/S0378-4371(02)01383-3>), the Sleep Regularity Index
(Phillips et al. (2017) <doi:10.1038/s41598-017-03171-4>), social jet lag,
rest-activity state transitions, and locomotor inactivity during sleep
(Winnebeck et al. (2018) <doi:10.1016/j.cub.2017.11.063>). It also reads
raw accelerometer files ('ActiGraph' '.gt3x', 'Axivity' '.cwa',
'GENEActiv' '.bin'), auto-calibrates them (van Hees et al. (2014)
<doi:10.1152/japplphysiol.00421.2014>), and derives the ENMO, MAD, and
z-angle metrics with diary-free sleep-period detection (van Hees et al.
(2018) <doi:10.1038/s41598-018-31266-z>), cross-checked against 'GGIR'. A
batch mode runs the analysis over a folder of files and writes a
multi-sheet 'Excel' workbook.

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
