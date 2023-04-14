%global __brp_check_rpaths %{nil}
%global packname  scorepeak
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Peak Functions for Peak Detection in Univariate Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-checkmate >= 1.9.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-checkmate >= 1.9.1
Requires:         R-CRAN-Rcpp >= 1.0.0

%description
Provides peak functions, which enable us to detect peaks in time series.
The methods implemented in this package are based on Girish Keshav
Palshikar (2009)
<https://www.researchgate.net/publication/228853276_Simple_Algorithms_for_Peak_Detection_in_Time-Series>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
