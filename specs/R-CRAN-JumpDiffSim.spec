%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  JumpDiffSim
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Jump Diffusion Simulation and Calibration for Merton and Kou Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.2
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 4.0.2
Requires:         R-CRAN-numDeriv >= 2016.8.1.1
Requires:         R-methods 
Requires:         R-stats 

%description
Implements the Merton (1976) <doi:10.1016/0304-405X(76)90022-2> and Kou
(2002) <doi:10.1287/mnsc.48.8.1086.166> jump-diffusion models through a
unified S4 object-oriented interface. Provides exact compound-Poisson
asset price simulation, maximum likelihood parameter estimation with
Hessian-based standard errors, Wald-type confidence intervals, European
option pricing via the Merton analytic series expansion, and
publication-quality diagnostic plots. All functionality operates entirely
offline without market data dependencies.

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
