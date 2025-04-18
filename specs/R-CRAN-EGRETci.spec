%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EGRETci
%global packver   2.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Exploration and Graphics for RivEr Trends Confidence Intervals

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-EGRET >= 3.0.5
BuildRequires:    R-CRAN-binom 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-EGRET >= 3.0.5
Requires:         R-CRAN-binom 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-foreach 

%description
Collection of functions to evaluate uncertainty of results from water
quality analysis using the Weighted Regressions on Time Discharge and
Season (WRTDS) method. This package is an add-on to the EGRET package that
performs the WRTDS analysis. The WRTDS modeling method was initially
introduced and discussed in Hirsch et al. (2010)
<doi:10.1111/j.1752-1688.2010.00482.x>, and expanded in Hirsch and De
Cicco (2015) <doi:10.3133/tm4A10>. The paper describing the uncertainty
and confidence interval calculations is Hirsch et al. (2015)
<doi:10.1016/j.envsoft.2015.07.017>.

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
