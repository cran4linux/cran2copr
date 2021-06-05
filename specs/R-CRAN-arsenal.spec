%global packname  arsenal
%global packver   3.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          An Arsenal of 'R' Functions for Large-Scale Statistical Summaries

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.4.0
BuildRequires:    R-utils >= 3.4.0
BuildRequires:    R-CRAN-knitr >= 1.29
Requires:         R-stats >= 3.4.0
Requires:         R-utils >= 3.4.0
Requires:         R-CRAN-knitr >= 1.29

%description
An Arsenal of 'R' functions for large-scale statistical summaries, which
are streamlined to work within the latest reporting tools in 'R' and
'RStudio' and which use formulas and versatile summary statistics for
summary tables and models. The primary functions include tableby(), a
Table-1-like summary of multiple variable types 'by' the levels of one or
more categorical variables; paired(), a Table-1-like summary of multiple
variable types paired across two time points; modelsum(), which performs
simple model fits on one or more endpoints for many variables (univariate
or adjusted for covariates); freqlist(), a powerful frequency table across
many categorical variables; comparedf(), a function for comparing
data.frames; and write2(), a function to output tables to a document.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
