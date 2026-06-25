%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mergeGridR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Grid-Based Number Merge Puzzle Simulation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggWebGL 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-tools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggWebGL 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-shiny 
Requires:         R-tools 

%description
Provides tools to simulate, analyse, visualise, and benchmark grid-based
number merge puzzles. The package implements generic grid mechanics,
tile-spawning rules, merge rules, scoring functions, reproducible
simulation utilities, and local 'Shiny' and 'WebGL' interfaces for
interactive use. It is intended for teaching, algorithmic experimentation,
and game-theoretic examples. The autoplay helpers use standard heuristic
search and Monte Carlo simulation ideas described in Russell and Norvig
(2021, ISBN:9780134610993) and Robert and Casella (2004,
ISBN:9780387212395).

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
