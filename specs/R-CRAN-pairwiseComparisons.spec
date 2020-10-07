%global packname  pairwiseComparisons
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Pairwise Comparison Tests

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ipmisc >= 4.0.0
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-PMCMRplus 
BuildRequires:    R-CRAN-parameters 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-WRS2 
Requires:         R-CRAN-ipmisc >= 4.0.0
Requires:         R-CRAN-BayesFactor 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-PMCMRplus 
Requires:         R-CRAN-parameters 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-WRS2 

%description
Multiple pairwise comparison tests on tidy data for one-way analysis of
variance for both between-subjects and within-subjects designs. Currently,
it supports only the most common types of statistical analyses and tests:
parametric (Welch's and Student's t-test), nonparametric (Durbin-Conover
and Dunn test), robust (Yuen’s trimmed means test), and Bayes Factor
(Student's t-test).

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
