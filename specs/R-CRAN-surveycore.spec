%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  surveycore
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Core Survey Analysis Infrastructure

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-tibble >= 3.1.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-pbivnorm >= 0.6.0
BuildRequires:    R-CRAN-marginaleffects >= 0.18.0
BuildRequires:    R-CRAN-S7 >= 0.1.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-tibble >= 3.1.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-pbivnorm >= 0.6.0
Requires:         R-CRAN-marginaleffects >= 0.18.0
Requires:         R-CRAN-S7 >= 0.1.0
Requires:         R-stats 
Requires:         R-graphics 

%description
A modern, 'S7'-based foundation for survey analysis spanning both
probability and non-probability samples. Probability sample designs
include Taylor series linearization, replicate weights (BRR, Fay,
jackknife, bootstrap), and two-phase estimation, following 'Lumley' (2004)
<doi:10.18637/jss.v009.i08>. Non-probability sample designs support
bootstrap and jackknife variance estimation for opt-in panels and
convenience samples. Provides a unified estimator interface for means,
frequencies, totals, quantiles, ratios, correlations, regression, and
t-tests, with weighted 'polychoric' and 'polyserial' correlation following
'Mannan' (2025) <doi:10.2139/ssrn.6580480>. A metadata system preserves
'haven'-style variable labels, value labels, and question-preface
attributes through all operations. Uses a 'tidyselect' interface
throughout.

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
