%global packname  detectR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Change Point Detection

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-LogConcDEAD 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-doParallel 
Requires:         R-graphics 
Requires:         R-CRAN-glasso 
Requires:         R-stats 
Requires:         R-CRAN-LogConcDEAD 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 

%description
Time series analysis of network connectivity. Detects and visualizes
change points between networks. Methods included in the package are
discussed in depth in Baek, C., Gates, K. M., Leinwand, B., Pipiras, V.
(2021) "Two sample tests for high-dimensional auto- covariances"
<doi:10.1016/j.csda.2020.107067> and Baek, C., Gampe, M., Leinwand B.,
Lindquist K., Hopfinger J. and Gates K. (2021) “Detecting functional
connectivity changes in fMRI data”. Preprint.

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
