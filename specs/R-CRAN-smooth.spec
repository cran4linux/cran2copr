%global packname  smooth
%global packver   2.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.0
Release:          2%{?dist}%{?buildtag}
Summary:          Forecasting Using State Space Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-forecast >= 7.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.8.100.0.0
BuildRequires:    R-CRAN-greybox >= 0.5.9
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-forecast >= 7.0
Requires:         R-CRAN-greybox >= 0.5.9
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-nloptr 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
Functions implementing Single Source of Error state space models for
purposes of time series analysis and forecasting. The package includes
Exponential Smoothing (Hyndman et al., 2008, <doi:
10.1007/978-3-540-71918-2>), SARIMA (Svetunkov & Boylan, 2019 <doi:
10.1080/00207543.2019.1600764>), Complex Exponential Smoothing (Svetunkov
& Kourentzes, 2018, <doi: 10.13140/RG.2.2.24986.29123>), Simple Moving
Average (Svetunkov & Petropoulos, 2018 <doi:
10.1080/00207543.2017.1380326>), Vector Exponential Smoothing (de Silva et
al., 2010, <doi: 10.1177/1471082X0901000401>) in state space forms,
several simulation functions and intermittent demand state space models.
It also allows dealing with intermittent demand based on the iETS
framework (Svetunkov & Boylan, 2017, <doi: 10.13140/RG.2.2.35897.06242>).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
