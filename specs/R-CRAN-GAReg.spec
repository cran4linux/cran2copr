%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GAReg
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Genetic Algorithms in Regression

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-splines 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-changepointGA 
BuildRequires:    R-CRAN-GA 
Requires:         R-stats 
Requires:         R-splines 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-changepointGA 
Requires:         R-CRAN-GA 

%description
Provides a genetic algorithm framework for regression problems requiring
discrete optimization over model spaces with unknown or varying dimension,
where gradient-based methods and exhaustive enumeration are impractical.
Uses a compact chromosome representation for tasks including spline knot
placement and best-subset variable selection, with constraint-preserving
crossover and mutation, exact uniform initialization under spacing
constraints, steady-state replacement, and optional island-model
parallelization from Lu, Lund, and Lee (2010, <doi:10.1214/09-AOAS289>).
The computation is built on the 'GA' engine of Scrucca (2017,
<doi:10.32614/RJ-2017-008>) and 'changepointGA' engine from Li and Lu
(2024, <doi:10.48550/arXiv.2410.15571>). In challenging high-dimensional
settings, 'GAReg' enables efficient search and delivers near-optimal
solutions when alternative algorithms are not well-justified.

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
