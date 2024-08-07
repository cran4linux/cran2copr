%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gets
%global packver   0.38
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.38
Release:          1%{?dist}%{?buildtag}
Summary:          General-to-Specific (GETS) Modelling and Indicator Saturation Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
Requires:         R-CRAN-zoo 
Requires:         R-parallel 
Requires:         R-methods 

%description
Automated General-to-Specific (GETS) modelling of the mean and variance of
a regression, and indicator saturation methods for detecting and testing
for structural breaks in the mean, see Pretis, Reade and Sucarrat (2018)
<doi:10.18637/jss.v086.i03> for an overview of the package. In advanced
use, the estimator and diagnostics tests can be fully user-specified, see
Sucarrat (2021) <doi:10.32614/RJ-2021-024>.

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
