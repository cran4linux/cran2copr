%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nonprobsampling
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Inference for Nonprobability Samples Using Multiple Reference Surveys

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-nleqslv 
Requires:         R-utils 

%description
Provides pseudo-weighted estimates of means and prevalences for finite
population inference from nonprobability samples using auxiliary
information from one or multiple probability reference surveys. The
package supports estimation with multiple reference surveys, allowing
auxiliary information to be combined when no single survey contains all
variables relevant to participation. Optional cumulative precalibration
can be applied to align weighted totals of shared variables across
surveys. Methods are based on the generalized estimating equations
framework of Landsman et al. (2026) <doi:10.1002/sim.70403> for correcting
participation bias. For a single reference survey, the package implements
the raking ratio calibration method and includes the adjusted logistic
propensity (ALP) method of Wang, Valliant, and Li (2021)
<doi:10.1002/sim.9122>, as well as the Chen-Li-Wu (CLW) method of Chen,
Li, and Wu (2020) <doi:10.1080/01621459.2019.1677241>. Analytic variance
estimation uses Taylor linearization and accounts for complex sampling
designs in the reference surveys via integration with the 'survey'
package.

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
