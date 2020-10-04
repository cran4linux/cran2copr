%global packname  TSPred
%global packver   4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Functions for Benchmarking Time Series Prediction

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-KFAS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-EMD 
BuildRequires:    R-CRAN-wavelets 
BuildRequires:    R-CRAN-vars 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-KFAS 
Requires:         R-stats 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-EMD 
Requires:         R-CRAN-wavelets 
Requires:         R-CRAN-vars 

%description
Functions for time series preprocessing, decomposition, prediction and
accuracy assessment using automatic linear modelling. The generated linear
models and its yielded prediction errors can be used for benchmarking
other time series prediction methods and for creating a demand for the
refinement of such methods. For this purpose, benchmark data from
prediction competitions may be used.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
