%global __brp_check_rpaths %{nil}
%global packname  DySS
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Screening Systems

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
In practice, we will encounter problems where the longitudinal performance
of processes needs to be monitored over time. Dynamic screening systems
(DySS) are methods that aim to identify and give signals to processes with
poor performance as early as possible. This package is designed to
implement dynamic screening systems and the related methods. References:
Qiu, P. and Xiang, D. (2014) <doi:10.1080/00401706.2013.822423>; Qiu, P.
and Xiang, D. (2015) <doi:10.1002/sim.6477>; Li, J. and Qiu, P. (2016)
<doi:10.1080/0740817X.2016.1146423>; Li, J. and Qiu, P. (2017)
<doi:10.1002/qre.2160>; You, L. and Qiu, P. (2019)
<doi:10.1080/00949655.2018.1552273>; Qiu, P., Xia, Z., and You, L. (2020)
<doi:10.1080/00401706.2019.1604434>; You, L., Qiu, A., Huang, B., and Qiu,
P. (2020) <doi:10.1002/bimj.201900127>; You, L. and Qiu, P. (2021)
<doi:10.1080/00224065.2020.1767006>.

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
