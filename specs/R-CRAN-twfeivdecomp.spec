%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  twfeivdecomp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Instrumented Difference-in-Differences Decomposition

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-AER 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 

%description
Implements a decomposition of the two-way fixed effects instrumental
variable estimator into all possible Wald difference-in-differences
estimators. Provides functions to summarize the contribution of different
cohort comparisons to the overall two-way fixed effects instrumental
variable estimate, with or without controls. The method is described in
Miyaji (2024) <doi:10.48550/arXiv.2405.16467>.

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
