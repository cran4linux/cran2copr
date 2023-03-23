%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  systemfit
%global packver   1.1-30
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.30
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Systems of Simultaneous Equations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sandwich >= 2.2.9
BuildRequires:    R-stats >= 2.14.0
BuildRequires:    R-CRAN-car >= 2.0.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
Requires:         R-CRAN-sandwich >= 2.2.9
Requires:         R-stats >= 2.14.0
Requires:         R-CRAN-car >= 2.0.0
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-MASS 
Requires:         R-methods 

%description
Econometric estimation of simultaneous systems of linear and nonlinear
equations using Ordinary Least Squares (OLS), Weighted Least Squares
(WLS), Seemingly Unrelated Regressions (SUR), Two-Stage Least Squares
(2SLS), Weighted Two-Stage Least Squares (W2SLS), and Three-Stage Least
Squares (3SLS) as suggested, e.g., by Zellner (1962)
<doi:10.2307/2281644>, Zellner and Theil (1962) <doi:10.2307/1911287>, and
Schmidt (1990) <doi:10.1016/0304-4076(90)90127-F>.

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
