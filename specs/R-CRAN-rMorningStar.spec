%global packname  rMorningStar
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          2%{?dist}%{?buildtag}
Summary:          Mutual Funds Performance Metrics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 

%description
Collection of functions to calculate performance metrics of mutual
funds/exchange traded funds. This package aids investors in researching
mutual funds/exchange traded funds for their investment decision. Also,
this package contains tools to manage a portfolio of different mutual
fund/exchange traded funds. For more information see Bruce J. Feibel
[2003, ISBN:978-0471445630].

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
