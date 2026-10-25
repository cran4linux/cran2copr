%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OptimalFactor
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Item Selection in Factor Analysis by Boosting and Specification Search

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides an iterative optimization algorithm for exploratory and
confirmatory factor analysis that follows a boosting approach inspired by
machine learning. It uses a composite fit index whose weights adapt to the
degrees of freedom and the sample size, following Kenny and McCoach (2003)
<doi:10.1207/S15328007SEM1003_1> and Shi, Lee and Maydeu-Olivares (2019)
<doi:10.1177/0013164418783530>. It detects and removes problematic items
(Heywood cases, cross-loadings, low loadings) with greedy or global search
strategies, checks interfactor correlations, and supports ordinal data
with WLSMV estimation and several rotation methods. A heuristic
specification search for confirmatory models (MacCallum, 1986
<doi:10.1037/0033-2909.100.1.107>) explores move, drop and covariance
operations across seed configurations. It also evaluates the resampling
stability of the item selection, the recovery of a known or theoretical
structure, and offers an optional conceptual analysis of removed items
through a large language model service.

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
