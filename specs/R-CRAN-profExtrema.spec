%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  profExtrema
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Compute and Visualize Profile Extrema Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-KrigInv 
BuildRequires:    R-CRAN-pGPx 
BuildRequires:    R-CRAN-microbenchmark 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-splines 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rcdd 
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-KrigInv 
Requires:         R-CRAN-pGPx 
Requires:         R-CRAN-microbenchmark 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-lhs 
Requires:         R-splines 
Requires:         R-methods 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rcdd 

%description
Computes profile extrema functions for arbitrary functions. If the
function is expensive-to-evaluate it computes profile extrema by emulating
the function with a Gaussian process (using package 'DiceKriging'). In
this case uncertainty quantification on the profile extrema can also be
computed. The different plotting functions for profile extrema give the
user a tool to better locate excursion sets.

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
