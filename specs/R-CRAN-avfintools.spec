%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  avfintools
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Financial Analysis Tools Using Data from 'Alpha Vantager'

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-methods >= 4.2.0
BuildRequires:    R-CRAN-plotly >= 4.10.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.6
BuildRequires:    R-CRAN-tibble >= 3.1.7
BuildRequires:    R-CRAN-lubridate >= 1.8.0
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-alphavantager >= 0.1.2
Requires:         R-methods >= 4.2.0
Requires:         R-CRAN-plotly >= 4.10.0
Requires:         R-CRAN-ggplot2 >= 3.3.6
Requires:         R-CRAN-tibble >= 3.1.7
Requires:         R-CRAN-lubridate >= 1.8.0
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-alphavantager >= 0.1.2

%description
To pull data from 'ALPHA VANTAGE' <https://www.alphavantage.co/>, use the
av_api_key() function from 'alphavantager' for inserting your API key.
This is a complement to the 'alphavantager' package from CRAN. Contains
commonly used quantitative finance tools. 'avfintools' stands for 'ALPHA
VANTAGE' Finance Tools, as it depends on sourcing financial data from the
'ALPHA VANTAGE' <https://www.alphavantage.co/documentation/> API.

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
