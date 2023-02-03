%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DecomposeR
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Empirical Mode Decomposition for Cyclostratigraphy

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-StratigrapheR >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-hexbin 
BuildRequires:    R-CRAN-colorRamps 
Requires:         R-CRAN-StratigrapheR >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-tictoc 
Requires:         R-grid 
Requires:         R-CRAN-hexbin 
Requires:         R-CRAN-colorRamps 

%description
Tools to apply Ensemble Empirical Mode Decomposition (EEMD) for
cyclostratigraphy purposes. Mainly: a new algorithm, extricate, that
performs EEMD in seconds, a linear interpolation algorithm using the
greatest rational common divisor of depth or time, different algorithms to
compute instantaneous amplitude, frequency and ratios of frequencies, and
functions to verify and visualise the outputs. The functions were
developed during the CRASH project (Checking the Reproducibility of
Astrochronology in the Hauterivian). When using for publication please
cite Wouters, S., Crucifix, M., Sinnesael, M., Da Silva, A.C., Zeeden, C.,
Zivanovic, M., Boulvain, F., Devleeschouwer, X., 2022, "A decomposition
approach to cyclostratigraphic signal processing". Earth-Science Reviews
225 (103894). <doi:10.1016/j.earscirev.2021.103894>.

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
