%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  enhancedTtest
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Enhanced T-Test with Automatic Selection and APA Formatting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car >= 3.0.0
BuildRequires:    R-CRAN-nortest >= 1.0.4
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-flextable >= 0.7.0
BuildRequires:    R-CRAN-htmltools >= 0.5.0
BuildRequires:    R-CRAN-officer >= 0.4.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-car >= 3.0.0
Requires:         R-CRAN-nortest >= 1.0.4
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-flextable >= 0.7.0
Requires:         R-CRAN-htmltools >= 0.5.0
Requires:         R-CRAN-officer >= 0.4.0
Requires:         R-stats 
Requires:         R-utils 

%description
Provides enhanced t-test functionality with automatic assumption checking,
non-parametric fallbacks, effect size calculation, and APA-formatted
tables that can be exported to Word documents. Supports one-sample,
two-sample, and paired t-tests with intelligent test selection. Effect
size interpretations follow Cohen (1988) <doi:10.4324/9780203771587> and
APA formatting follows the Publication Manual of the American
Psychological Association, 7th edition (2020) <doi:10.1037/0000165-000>.

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
