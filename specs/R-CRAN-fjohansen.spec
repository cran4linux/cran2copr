%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fjohansen
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Johansen Cointegration Test with Fourier-Type Smooth Nonlinear Trends

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-scales 

%description
Implements the Johansen cointegration test with Fourier-type smooth
nonlinear deterministic trends restricted to cointegrating relations, as
developed by Kurita and Shintani (2025)
<doi:10.1080/07474938.2025.2530640>. Six model variants are supported: CNR
(constant plus nonlinear, restricted in the cointegrating space), LNR
(linear plus nonlinear, restricted), CNU (constant restricted, nonlinear
unrestricted), LNU (linear restricted, nonlinear unrestricted), plus the
standard constant- and linear-trend restricted Johansen models. The
package also bundles the feasible generalised least squares (FGLS) Wald
test of Perron, Shintani and Yabu (2017) <doi:10.1111/obes.12169> used as
a frequency-selection pre-step, together with bundled critical-value
tables, a vectorised simulator for the limiting distribution,
publication-quality table exports (LaTeX and HTML) and 'ggplot2' figures
matching those of the paper.

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
