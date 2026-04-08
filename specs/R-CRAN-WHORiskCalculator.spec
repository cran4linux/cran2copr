%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WHORiskCalculator
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          WHO Cardiovascular Disease Risk Calculator

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Implements the 2019 World Health Organization (WHO) cardiovascular disease
(CVD) risk prediction models, as described in Kaptoge et al. (2019)
<doi:10.1016/S2214-109X(19)30318-3>. Provides two validated models for
estimating 10-year risk of fatal and non-fatal cardiovascular events
(myocardial infarction and stroke): a laboratory-based model using age,
sex, systolic blood pressure, total cholesterol, smoking status, and
diabetes history; and a non-laboratory-based model substituting body mass
index (BMI) for cholesterol and diabetes, suitable for resource-limited
settings. Risk estimates are recalibrated to 21 Global Burden of Disease
regions using region-specific incidence rates and risk factor
distributions derived from the Emerging Risk Factors Collaboration.
Functions are fully vectorized for efficient batch calculations and
support automatic country-to-region mapping via ISO 3166-1 alpha-3 country
codes.

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
