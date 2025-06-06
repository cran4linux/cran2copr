%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forsearch
%global packver   6.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Diagnostic Analysis Using Forward Search Procedure for Various Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 5.2.1
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-survival >= 3.3.3
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-nlme >= 3.1.166
BuildRequires:    R-CRAN-formula.tools >= 1.7.1
BuildRequires:    R-CRAN-Cairo >= 1.6.2
BuildRequires:    R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-Hmisc >= 5.2.1
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-survival >= 3.3.3
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-nlme >= 3.1.166
Requires:         R-CRAN-formula.tools >= 1.7.1
Requires:         R-CRAN-Cairo >= 1.6.2
Requires:         R-CRAN-rlang >= 1.1.4

%description
Identifies potential data outliers and their impact on estimates and
analyses. Tool for evaluation of study credibility. Uses the forward
search approach of Atkinson and Riani, "Robust Diagnostic Regression
Analysis", 2000,<ISBN: o-387-95017-6> to prepare descriptive statistics of
a dataset that is to be analyzed by functions lm {stats}, glm {stats}, nls
{stats}, lme {nlme}, or coxph {survival}, or their equivalent in another
language.  Includes graphics functions to display the descriptive
statistics.

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
