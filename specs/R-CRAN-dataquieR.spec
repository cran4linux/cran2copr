%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dataquieR
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Quality in Epidemiological Research

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-MultinomialCI 
BuildRequires:    R-CRAN-parallelMap 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-R.devices 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-qmrparser 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-MultinomialCI 
Requires:         R-CRAN-parallelMap 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-R.devices 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-qmrparser 
Requires:         R-utils 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-scales 

%description
Data quality assessments guided by a 'data quality framework introduced by
Schmidt and colleagues, 2021' <doi:10.1186/s12874-021-01252-7> target the
data quality dimensions integrity, completeness, consistency, and
accuracy. The scope of applicable functions rests on the availability of
extensive metadata which can be provided in spreadsheet tables. Either
standardized (e.g. as 'html5' reports) or individually tailored reports
can be generated. For an introduction into the specification of
corresponding metadata, please refer to the 'package website'
<https://dataquality.ship-med.uni-greifswald.de/Annotation_of_Metadata.html>.

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
