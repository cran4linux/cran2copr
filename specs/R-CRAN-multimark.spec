%global __brp_check_rpaths %{nil}
%global packname  multimark
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Capture-Mark-Recapture Analysis using Multiple Non-Invasive Marks

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-RMark 
BuildRequires:    R-CRAN-Brobdingnag 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
Requires:         R-parallel 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-RMark 
Requires:         R-CRAN-Brobdingnag 
Requires:         R-CRAN-mvtnorm 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 

%description
Traditional and spatial capture-mark-recapture analysis with multiple
non-invasive marks. The models implemented in 'multimark' combine
encounter history data arising from two different non-invasive "marks",
such as images of left-sided and right-sided pelage patterns of
bilaterally asymmetrical species, to estimate abundance and related
demographic parameters while accounting for imperfect detection. Bayesian
models are specified using simple formulae and fitted using Markov chain
Monte Carlo. Addressing deficiencies in currently available software,
'multimark' also provides a user-friendly interface for performing
Bayesian multimodel inference using non-spatial or spatial
capture-recapture data consisting of a single conventional mark or
multiple non-invasive marks. See McClintock (2015) <doi:10.1002/ece3.1676>
and Maronde et al. (2020) <doi:10.1002/ece3.6990>.

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
