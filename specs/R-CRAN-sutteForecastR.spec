%global packname  sutteForecastR
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Forecasting Data using Alpha-Sutte Indicator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-fracdiff 
BuildRequires:    R-CRAN-robets 
BuildRequires:    R-CRAN-forecastHybrid 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-fracdiff 
Requires:         R-CRAN-robets 
Requires:         R-CRAN-forecastHybrid 

%description
The alpha-Sutte indicator (alpha-Sutte) was originally from developed of
Sutte indicator. Sutte indicator can using to predict the movement of
stocks. As the development of science, then Sutte indicator developed to
predict not only the movement of stocks but also can forecast data on
financial, insurance, and others time series data. Ahmar, A.S. (2017)
<doi:10.17605/osf.io/rknsv>.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
