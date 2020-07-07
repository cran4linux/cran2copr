%global packname  tsfeatures
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}
Summary:          Time Series Feature Extraction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.3
BuildRequires:    R-CRAN-RcppRoll >= 0.2.2
BuildRequires:    R-CRAN-fracdiff 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-furrr 
Requires:         R-CRAN-forecast >= 8.3
Requires:         R-CRAN-RcppRoll >= 0.2.2
Requires:         R-CRAN-fracdiff 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-urca 
Requires:         R-CRAN-future 
Requires:         R-CRAN-furrr 

%description
Methods for extracting various features from time series data. The
features provided are those from Hyndman, Wang and Laptev (2013)
<doi:10.1109/ICDMW.2015.104>, Kang, Hyndman and Smith-Miles (2017)
<doi:10.1016/j.ijforecast.2016.09.004> and from Fulcher, Little and Jones
(2013) <doi:10.1098/rsif.2013.0048>. Features include spectral entropy,
autocorrelations, measures of the strength of seasonality and trend, and
so on. Users can also define their own feature functions.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
