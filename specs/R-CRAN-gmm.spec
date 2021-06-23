%global __brp_check_rpaths %{nil}
%global packname  gmm
%global packver   1.6-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.6
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Method of Moments and Generalized Empirical Likelihood

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
It is a complete suite to estimate models based on moment conditions. It
includes the two step Generalized method of moments (Hansen 1982;
<doi:10.2307/1912775>), the iterated GMM and continuous updated estimator
(Hansen, Eaton and Yaron 1996; <doi:10.2307/1392442>) and several methods
that belong to the Generalized Empirical Likelihood family of estimators
(Smith 1997; <doi:10.1111/j.0013-0133.1997.174.x>, Kitamura 1997;
<doi:10.1214/aos/1069362388>, Newey and Smith 2004;
<doi:10.1111/j.1468-0262.2004.00482.x>, and Anatolyev 2005
<doi:10.1111/j.1468-0262.2005.00601.x>).

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
