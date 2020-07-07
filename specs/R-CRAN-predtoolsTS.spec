%global packname  predtoolsTS
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Time Series Prediction Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TSPred 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-utils 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-forecast 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-Metrics 
Requires:         R-stats 
Requires:         R-CRAN-TSPred 
Requires:         R-CRAN-tseries 
Requires:         R-utils 

%description
Makes the time series prediction easier by automatizing this process using
four main functions: prep(), modl(), pred() and postp(). Features
different preprocessing methods to homogenize variance and to remove trend
and seasonality. Also has the potential to bring together different
predictive models to make comparatives. Features ARIMA and Data Mining
Regression models (using caret).

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
