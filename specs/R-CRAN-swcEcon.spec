%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  swcEcon
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Economic Analysis of Soil and Water Conservation Measures in Watersheds

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Provides functions and benchmark datasets for the economic appraisal of
soil and water conservation (SWC) measures in watershed development
projects. Implements benefit-cost ratio (BCR), net present value (NPV),
internal rate of return (IRR) via the bisection method of Brent (1973,
ISBN:9780130223715), modified BCR, marginal rate of return using the
CIMMYT (1988, ISBN:9686127127) method, payback period, soil loss economic
valuation via the Universal Soil Loss Equation of Wischmeier and Smith
(1978, ISBN:0160016258), groundwater recharge valuation, employment
generation ratio, sensitivity analysis, switching value analysis, and
Monte Carlo simulation. Six datasets are included: state-wise BCR
benchmarks from NABARD (2019) watershed evaluations, USLE erodibility
parameters for Indian soil orders from NBSS and LUP, rainfall erosivity
for twenty Indian districts from IMD data, SWC unit cost norms from
PMKSY-WDC (GoI 2015), and two hypothetical datasets for illustration.
Methods follow Gittinger (1982, ISBN:9780801825439) and Squire and van der
Tak (1975, ISBN:9780801816697).

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
