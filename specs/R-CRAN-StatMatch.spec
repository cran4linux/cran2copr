%global packname  StatMatch
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          3%{?dist}
Summary:          Statistical Matching or Data Fusion

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7.0
Requires:         R-core >= 2.7.0
BuildArch:        noarch
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-lpSolve 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-lpSolve 

%description
Integration of two data sources referred to the same target population
which share a number of variables. Some functions can also be used to
impute missing values in data sets through hot deck imputation methods.
Methods to perform statistical matching when dealing with data from
complex sample surveys are available too.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
