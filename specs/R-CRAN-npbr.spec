%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  npbr
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Boundary Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rglpk >= 0.6.2
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Benchmarking 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-splines 
Requires:         R-CRAN-Rglpk >= 0.6.2
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Benchmarking 
Requires:         R-CRAN-np 
Requires:         R-CRAN-quadprog 
Requires:         R-splines 

%description
A variety of functions for the best known and most innovative approaches
to nonparametric boundary estimation. The selected methods are concerned
with empirical, smoothed, unrestricted as well as constrained fits under
both separate and multiple shape constraints. They cover robust approaches
to outliers as well as data envelopment techniques based on piecewise
polynomials, splines, local linear fitting, extreme values and kernel
smoothing. The package also seamlessly allows for Monte Carlo comparisons
among these different estimation methods.  Its use is illustrated via a
number of empirical applications and simulated examples.

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
