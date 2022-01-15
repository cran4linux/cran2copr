%global __brp_check_rpaths %{nil}
%global packname  cpsurvsim
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulating Survival Data from Change-Point Hazard Distributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 4.3.0
BuildRequires:    R-CRAN-plyr >= 1.8.5
BuildRequires:    R-CRAN-knitr >= 1.27
BuildRequires:    R-stats 
Requires:         R-CRAN-Hmisc >= 4.3.0
Requires:         R-CRAN-plyr >= 1.8.5
Requires:         R-CRAN-knitr >= 1.27
Requires:         R-stats 

%description
Simulates time-to-event data with type I right censoring using two
methods: the inverse CDF method and our proposed memoryless method. The
latter method takes advantage of the memoryless property of survival and
simulates a separate distribution between change-points. We include two
parametric distributions: exponential and Weibull. Inverse CDF method
draws on the work of Rainer Walke (2010),
<https://www.demogr.mpg.de/papers/technicalreports/tr-2010-003.pdf>.

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
