%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scoringutils
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for Scoring and Assessing Predictions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-data.table >= 1.16.0
BuildRequires:    R-CRAN-scoringRules >= 1.1.3
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-data.table >= 1.16.0
Requires:         R-CRAN-scoringRules >= 1.1.3
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-methods 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-purrr 
Requires:         R-stats 

%description
Facilitate the evaluation of forecasts in a convenient framework based on
data.table. It allows user to to check their forecasts and diagnose
issues, to visualise forecasts and missing data, to transform data before
scoring, to handle missing forecasts, to aggregate scores, and to
visualise the results of the evaluation. The package mostly focuses on the
evaluation of probabilistic forecasts and allows evaluating several
different forecast types and input formats. Find more information about
the package in the Vignettes as well as in the accompanying paper,
<doi:10.48550/arXiv.2205.07090>.

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
