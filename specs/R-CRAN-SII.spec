%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SII
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate ANSI/ASA S3.5-1997 (R2024) Speech Intelligibility Index

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
Calculates the American National Standards Institute (ANSI) S3.5-1997
Speech Intelligibility Index (SII) (ANSI, 1997), a standard method for
computing the intelligibility of speech from acoustical measurements of
speech, noise, and hearing thresholds. This package includes data frames
corresponding to Tables 1 - 4 in the ANSI standard as well as functions
utilizing these tables and user-provided hearing threshold and noise level
measurements to compute the SII score. The methods implemented here extend
the standard computations to allow calculation of SII when the measured
frequencies do not match those required by the standard by applying
interpolation. The package also includes a native C++ implementation of
the 'AUDMOD' specific loudness model for impaired hearing (Bramslow,
2004), ported from the 'bramslow2004' implementation in the Auditory
Modeling Toolbox (AMT), to calculate loudness in sones. It provides
methods to predict aided SII under hearing aid prescriptive rationales,
including Open-NL (Open Non-Linear), a theoretical optimization framework
that uses a Nelder-Mead simplex search to maximize the SII (by default
with the Johnson and Dillon (2011) desensitization correction), subject to
loudness penalties and simulated Maximum Power Output (MPO) constraints.
Further functions calculate real-ear insertion gains, estimate maximum
power output (SSPL90), and prescribe dynamic range compression. Open-NL
and the prescription functions are research tools for theoretical modeling
and simulation; they have not been clinically validated and are not
intended for fitting hearing aids to patients. Development of this package
was originally funded by the Center for Bioscience Education and
Technology (CBET) of the Rochester Institute of Technology (RIT).

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
