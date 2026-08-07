%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qtsa
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Quantum Time Series Analysis: Drift, Noise Spectroscopy and Calibration Forecasting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Tools for exploratory statistical analysis of quantum-hardware calibration
time series. The package provides simulators for random telegraph noise
(RTN), power-law noise, and Ornstein-Uhlenbeck dephasing; Welch and
sine-multitaper power spectral density estimators; a lightweight two-state
hidden Markov model for switching signals; cumulative sum (CUSUM) and
binary-segmentation diagnostics for calibration drift; residual-quantile
interval forecasts; and filter-function calculations for illustrative
coherence curves. The package includes a reproducible generator of
simulated superconducting-qubit calibration records; it does not retrieve
authenticated live provider data. Methodological background is provided by
Welch (1967) <doi:10.1109/TAU.1967.1161901>, Thomson (1982)
<doi:10.1109/PROC.1982.12433>, Rabiner (1989) <doi:10.1109/5.18626>, Page
(1954) <doi:10.1093/biomet/41.1-2.100>, Paladino et al. (2014)
<doi:10.1103/RevModPhys.86.361>, and Cywinski et al. (2008)
<doi:10.1103/PhysRevB.77.174509>.

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
