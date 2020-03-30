%global packname  greybox
%global packver   0.5.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.9
Release:          1%{?dist}
Summary:          Toolbox for Model Building and Forecasting

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lamW 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-forecast 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-lamW 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-statmod 

%description
Implements functions and instruments for regression model building and its
application to forecasting. The main scope of the package is in variables
selection and models specification for cases of time series data. This
includes promotional modelling, selection between different dynamic
regressions with non-standard distributions of errors, selection based on
cross validation, solutions to the fat regression model problem and more.
Models developed in the package are tailored specifically for forecasting
purposes. So as a results there are several methods that allow producing
forecasts from these models and visualising them.

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
