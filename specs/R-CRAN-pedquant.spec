%global __brp_check_rpaths %{nil}
%global packname  pedquant
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Public Economic Data and Quantitative Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-TTR 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-TTR 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-plotly 

%description
Provides an interface to access public economic and financial data for
economic research and quantitative analysis. The data sources including
NBS, FRED, Yahoo Finance, 163 Finance and etc.

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
