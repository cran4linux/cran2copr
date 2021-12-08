%global __brp_check_rpaths %{nil}
%global packname  MFSIS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Moder-Free Sure Independent Screening Procedures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Ball 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pkgdown 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Ball 
Requires:         R-CRAN-reticulate 
Requires:         R-stats 
Requires:         R-CRAN-pkgdown 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dr 

%description
An implementation of popular screening methods that are commonly employed
in ultra-high and high dimensional data. Through this publicly available
package, we provide a unified framework to carry out model-free screening
procedures including SIS (Fan and Lv (2008)
<doi:10.1111/j.1467-9868.2008.00674.x>), SIRS(Zhu et al.
(2011)<doi:10.1198/jasa.2011.tm10563>), DC-SIS (Li et al. (2012)
<doi:10.1080/01621459.2012.695654>), MDC-SIS(Shao and Zhang (2014)
<doi:10.1080/01621459.2014.887012>), Bcor-SIS (Pan et al. (2019)
<doi:10.1080/01621459.2018.1462709>), PC-Screen (Liu et al. (2020)
<doi:10.1080/01621459.2020.1783274>), WLS (Zhong et al.(2021)
<doi:10.1080/01621459.2021.1918554>), Kfilter (Mai and Zou (2015)
<doi:10.1214/14-AOS1303>), MVSIS (Cui et al. (2015)
<doi:10.1080/01621459.2014.920256>) and CSIS.

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
