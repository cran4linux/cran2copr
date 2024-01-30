%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AnalysisLin
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Data Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RANN 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-stats 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RANN 

%description
A quick and effective data exploration toolkit. It provides essential
features, including a descriptive statistics table for a quick overview of
your dataset, interactive distribution plots to visualize variable
patterns, Principal Component Analysis for dimensionality reduction and
feature analysis, missing value imputation methods, and correlation
analysis.

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
