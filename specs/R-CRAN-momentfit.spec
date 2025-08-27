%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  momentfit
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Methods of Moments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-parallel 

%description
Several classes for moment-based models are defined. The classes are
defined for moment conditions derived from a single equation or a system
of equations. The conditions can also be expressed as functions or
formulas. Several methods are also offered to facilitate the development
of different estimation techniques. The methods that are currently
provided are the Generalized method of moments (Hansen 1982;
<doi:10.2307/1912775>), for single equations and systems of equation, and
the Generalized Empirical Likelihood (Smith 1997;
<doi:10.1111/j.0013-0133.1997.174.x>, Kitamura 1997;
<doi:10.1214/aos/1069362388>, Newey and Smith 2004;
<doi:10.1111/j.1468-0262.2004.00482.x>, and Anatolyev 2005
<doi:10.1111/j.1468-0262.2005.00601.x>). Some work is being done to add
tools to deal with weak and/or many instruments. This includes K-Class
estimators (Limited Information Maximum Likelihood and Fuller), Anderson
and Rubin statistic test, etc.

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
