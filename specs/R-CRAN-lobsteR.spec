%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lobsteR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access and Process 'LOBSTER' High-Frequency Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-archive 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-timeDate 
Requires:         R-CRAN-archive 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-timeDate 

%description
Provides tools to authenticate with 'LOBSTER' (Limit Order Book System -
The Efficient Reconstruction, <https://app.lobsterdata.com/>), request,
download, and process high-frequency limit order book data. Streamlines
the end-to-end workflow from data request to analysis-ready datasets. For
advanced high-frequency econometric analysis, see the 'highfrequency'
package.

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
