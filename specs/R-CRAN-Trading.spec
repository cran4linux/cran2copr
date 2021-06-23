%global __brp_check_rpaths %{nil}
%global packname  Trading
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}%{?buildtag}
Summary:          CCR, Entropy-Based Correlation Estimates & Dynamic Beta

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-PerformanceAnalytics 
Requires:         R-methods 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-PerformanceAnalytics 

%description
Contains performance analysis metrics of track records including
entropy-based correlation and dynamic beta based on the Kalman filter. The
normalized sample entropy method has been implemented which produces
accurate entropy estimation even on smaller datasets while for the dynamic
beta calculation the Kalman filter methodology has been utilized. On a
separate stream, trades from the five major assets classes and also
functionality to use pricing curves, rating tables, CSAs and add-on
tables. The implementation follows an object oriented logic whereby each
trade inherits from more abstract classes while also the curves/tables are
objects. There is a lot of functionality focusing on the counterparty
credit risk calculations however the package can be used for trading
applications in general.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
