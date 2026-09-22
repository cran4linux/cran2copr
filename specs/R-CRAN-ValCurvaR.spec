%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ValCurvaR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Validation of Analytical Calibration Curves

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-outliers 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-outliers 
Requires:         R-stats 

%description
Provides transparent tools for fitting and evaluating analytical
calibration curves. Ordinary and weighted least squares fits are
supported, together with lack-of-fit, heteroscedasticity and influence
diagnostics, back-calculation, prediction uncertainty and
publication-ready base graphics. The workflow is designed to support
validation studies rather than rely on a single goodness-of-fit statistic.
Methods follow Magnusson and Ornemark (2014)
<https://www.eurachem.org/images/stories/Guides/pdf/MV_guide_2nd_ed_EN.pdf>
and International Council for Harmonisation (2023)
<https://database.ich.org/sites/default/files/ICH_Q2%%28R2%%29_Guideline_2023_1130_ErrorCorrection_2025.pdf>.

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
