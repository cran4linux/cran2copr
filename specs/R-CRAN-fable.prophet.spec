%global __brp_check_rpaths %{nil}
%global packname  fable.prophet
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Prophet Modelling Interface for 'fable'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-fabletools >= 0.2.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tsibble 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-prophet 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-distributional 
Requires:         R-CRAN-fabletools >= 0.2.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tsibble 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-prophet 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-distributional 

%description
Allows prophet models from the 'prophet' package to be used in a tidy
workflow with the modelling interface of 'fabletools'. This extends
'prophet' to provide enhanced model specification and management,
performance evaluation methods, and model combination tools.

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
