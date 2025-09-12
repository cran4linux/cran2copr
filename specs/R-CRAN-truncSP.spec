%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  truncSP
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Semi-Parametric Estimators of Truncated Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-truncreg 
BuildRequires:    R-CRAN-boot 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-truncreg 
Requires:         R-CRAN-boot 

%description
Estimators for semi-parametric linear regression models with truncated
response variables (fixed truncation point). The estimators implemented
are the Symmetrically Trimmed Least Squares (STLS) estimator introduced by
Powell (1986) <doi:10.2307/1914308>, the Quadratic Mode (QME) estimator
introduced by Lee (1993) <doi:10.1016/0304-4076(93)90056-B>, and the Left
Truncated (LT) estimator introduced by Karlsson (2006)
<doi:10.1007/s00184-005-0023-x>.

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
