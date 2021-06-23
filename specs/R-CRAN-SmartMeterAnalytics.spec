%global __brp_check_rpaths %{nil}
%global packname  SmartMeterAnalytics
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Smart Meter Data Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-stinepack 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-stinepack 
Requires:         R-CRAN-zoo 

%description
Methods for analysis of energy consumption data (electricity, gas, water)
at different data measurement intervals. The package provides feature
extraction methods and algorithms to prepare data for data mining and
machine learning applications. Deatiled descriptions of the methods and
their application can be found in Hopf (2019, ISBN:978-3-86309-669-4)
"Predictive Analytics for Energy Efficiency and Energy Retailing"
<doi:10.20378/irbo-54833> and Hopf et al. (2016)
<doi:10.1007/s12525-018-0290-9> "Enhancing energy efficiency in the
residential sector with smart meter data analytics".

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
