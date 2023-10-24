%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PSAboot
%global packver   1.3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.8
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrapping for Propensity Score Analysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-PSAgraphics 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-Matching 
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-CRAN-modeltools 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TriMatch 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-PSAgraphics 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-Matching 
Requires:         R-CRAN-MatchIt 
Requires:         R-CRAN-modeltools 
Requires:         R-parallel 
Requires:         R-CRAN-party 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rpart 
Requires:         R-stats 
Requires:         R-CRAN-TriMatch 
Requires:         R-utils 

%description
It is often advantageous to test a hypothesis more than once in the
context of propensity score analysis (Rosenbaum, 2012)
<doi:10.1093/biomet/ass032>. The functions in this package facilitate
bootstrapping for propensity score analysis (PSA). By default,
bootstrapping using two classification tree methods (using 'rpart' and
'ctree' functions), two matching methods (using 'Matching' and 'MatchIt'
packages), and stratification with logistic regression.  A framework is
described for users to implement additional propensity score methods.
Visualizations are emphasized for diagnosing balance; exploring the
correlation relationships between bootstrap samples and methods; and to
summarize results.

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
