%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ivcheck
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tests for Instrumental Variable Validity

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-stats 
Requires:         R-parallel 

%description
Implements tests for the identifying assumptions of instrumental variable
models, the local exclusion restriction and monotonicity conditions
required for local average treatment effect identification. Covers
Kitagawa (2015) <doi:10.3982/ECTA11974>, Mourifie and Wan (2017)
<doi:10.1162/REST_a_00622>, and Frandsen, Lefgren, and Leslie (2023)
<doi:10.1257/aer.20201860>. Includes a one-shot wrapper that runs all
applicable tests on a fitted instrumental variable model. Dispatches on
'fixest' and 'ivreg' model objects.

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
