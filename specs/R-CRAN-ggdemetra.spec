%global __brp_check_rpaths %{nil}
%global packname  ggdemetra
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          'ggplot2' Extension for Seasonal and Trading Day Adjustment with 'RJDemetra'

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-RJDemetra >= 0.1.2
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-RJDemetra >= 0.1.2
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-gridExtra 

%description
Provides 'ggplot2' functions to return the results of seasonal and trading
day adjustment made by 'RJDemetra'. 'RJDemetra' is an 'R' interface around
'JDemetra+' (<https://github.com/jdemetra/jdemetra-app>), the seasonal
adjustment software officially recommended to the members of the European
Statistical System and the European System of Central Banks.

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
