%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ThresholdROC
%global packver   2.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Optimum Threshold Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-ks 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-ks 

%description
Functions that provide point and interval estimations of optimum
thresholds for continuous diagnostic tests. The methodology used is based
on minimizing an overall cost function in the two- and three-state
settings. We also provide functions for sample size determination and
estimation of diagnostic accuracy measures. We also include graphical
tools. The statistical methodology used here can be found in Perez-Jaume
et al (2017) <doi:10.18637/jss.v082.i04> and in Skaltsa et al (2010, 2012)
<doi:10.1002/bimj.200900294>, <doi:10.1002/sim.4369>.

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
