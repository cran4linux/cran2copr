%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robotstxtr
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Engine-Aware 'robots.txt' Policy with Google's Matcher Algorithm

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-rurl >= 3.0.1
BuildRequires:    R-CRAN-httr2 >= 1.2.0
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-rurl >= 3.0.1
Requires:         R-CRAN-httr2 >= 1.2.0

%description
Evaluates whether URLs may be crawled according to 'robots.txt' rules. A
versioned engine-aware facade keeps neutral fetch evidence, per-engine
status policy, robots product tokens, and matcher capabilities separate,
returning explicit non-decisions when policy is undocumented or a matcher
is unavailable. The available matcher is a bundled,
upstream-test-validated snapshot of Google's open-source C++ 'robots.txt'
matcher, preserving 'Googlebot' behavior. Fetches use a deterministic,
conservative policy built on 'httr2', with fetch origins constructed by
'rurl'. All network access in tests, examples, and vignettes is mocked or
served locally, so no internet connection is required to install, test, or
check the package. This matcher derives from Google's 'robotstxt' project
<https://github.com/google/robotstxt>, distributed under the Apache
License 2.0; see the package NOTICE.

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
