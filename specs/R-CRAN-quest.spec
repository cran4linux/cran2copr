%global __brp_check_rpaths %{nil}
%global packname  quest
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Prepare Questionnaire Data for Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-datasets 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-str2str 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-psychTools 
Requires:         R-datasets 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-str2str 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-car 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-psychTools 

%description
Offers a suite of functions to prepare questionnaire data for analysis
(perhaps other types of data as well). By data preparation, I mean data
analytic tasks to get your raw data ready for statistical modeling (e.g.,
regression). There are functions to investigate missing data, reshape
data, validate responses, recode variables, score questionnaires, center
variables, aggregate by groups, shift scores (i.e., leads or lags), etc.
It provides functions for both single level and multilevel (i.e., grouped)
data. With a few exceptions (e.g., ncases()), functions without an "s" at
the end of their primary word (e.g., center_by()) act on atomic vectors,
while functions with an "s" at the end of their primary word (e.g.,
centers_by()) act on multiple columns of a data.frame.

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
