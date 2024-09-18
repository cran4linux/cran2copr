%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WAnova
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Welch's Anova from Summary Statistics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-SuppDists 
Requires:         R-CRAN-car 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-SuppDists 

%description
Provides the functions to perform a Welch's one-way Anova with fixed
effects based on summary statistics (sample size, means, standard
deviation) and the Games-Howell post hoc test for multiple comparisons and
provides the effect size estimator adjusted omega squared. In addition
sample size estimation can be computed based on Levy's method, and a Monte
Carlo simulation is included to bootstrap residual normality and
homoscedasticity Welch, B. L. (1951) <doi:10.1093/biomet/38.3-4.330> Kirk,
R. E. (1996) <doi:10.1177/0013164496056005002> Carroll, R. M., & Nordholm,
L. A. (1975) <doi:10.1177/001316447503500304> Albers, C., & Lakens, D.
(2018) <doi:10.1016/j.jesp.2017.09.004> Games, P. A., & Howell, J. F.
(1976) <doi:10.2307/1164979> Levy, K. J. (1978a)
<doi:10.1080/00949657808810246> Show-Li, J., & Gwowen, S. (2014)
<doi:10.1111/bmsp.12006>.

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
