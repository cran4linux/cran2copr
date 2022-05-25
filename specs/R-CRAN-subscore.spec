%global __brp_check_rpaths %{nil}
%global packname  subscore
%global packver   3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Computing Subscores in Classical Test Theory and Item Response Theory

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CTT 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-irtoys 
BuildRequires:    R-CRAN-sirt 
BuildRequires:    R-CRAN-ltm 
BuildRequires:    R-CRAN-cocor 
BuildRequires:    R-CRAN-boot 
Requires:         R-CRAN-CTT 
Requires:         R-stats 
Requires:         R-CRAN-irtoys 
Requires:         R-CRAN-sirt 
Requires:         R-CRAN-ltm 
Requires:         R-CRAN-cocor 
Requires:         R-CRAN-boot 

%description
Functions for computing test subscores using different methods in both
classical test theory (CTT) and item response theory (IRT). This package
enables three types of subscoring methods within the framework of CTT and
IRT, including (1) Wainer's augmentation method (Wainer et. al., 2001)
<doi:10.4324/9781410604729>, (2) Haberman's subscoring methods (Haberman,
2008) <doi:10.3102/1076998607302636>, and (3) Yen's objective performance
index (OPI; Yen, 1987)
<https://www.ets.org/research/policy_research_reports/publications/paper/1987/hrap>.
It also includes functions to compute Proportional Reduction of Mean
Squared Errors (PRMSEs) in Haberman's methods which are used to examine
whether test subscores are of added value. In addition, the package
includes a function to assess the local independence assumption of IRT
with Yen's Q3 statistic (Yen, 1984 <doi:10.1177/014662168400800201>; Yen,
1993 <doi:10.1111/j.1745-3984.1993.tb00423.x>).

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
