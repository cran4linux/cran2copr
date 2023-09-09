%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SurveyCC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Canonical Correlation for Survey Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-candisc 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survey 
Requires:         R-CRAN-candisc 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-survey 

%description
Performs canonical correlation for survey data, including multiple tests
of significance for secondary canonical correlations. A key feature of
this package is that it incorporates survey data structure directly in a
novel test of significance via a sequence of simple linear regression
models on the canonical variates. See references - Cruz-Cano and
Mead-Morse (2023) "Canonical Correlation Analysis for Complex Survey data"
The Stata Journal under review. Gentzke AS, Wang TW, Cornelius M, Park-Lee
E, Ren C, Sawdey MD, Cullen KA, Loretan C, Jamal A, Homa DM (2021)
"Tobacco Product Use and Associated Factors among Middle and High School
Students - National Youth Tobacco Survey, United States"
<doi:10.15585/mmwr.ss7105a1>. Gittins R (1986 ISBN:3642698786,
9783642698781). Caliński T., Krzyśko M. and WOłyński W. (2006) "A
Comparison of Some Tests for Determining the Number of Nonzero Canonical
Correlations" <doi:10.1080/03610910600716290>. Hyland A, Ambrose BK,
Conway KP, et al. (2017) "Design and methods of the Population Assessment
of Tobacco and Health" <doi:10.1136/tobaccocontrol-2016-052934>. Johnstone
IM. (2009) "Approximate Null Distribution of the largest root in a
Multivariate Analysis" <doi:10.1214/08-AOAS220>. Valliant R. and Dever JA.
(2018 ISBN:978-1-59718-260-7).

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
