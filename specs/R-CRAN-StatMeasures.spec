%global packname  StatMeasures
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Easy Data Manipulation, Data Quality and Statistical Checks

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.4
Requires:         R-CRAN-data.table >= 1.9.4

%description
Offers useful functions to perform day-to-day data manipulation
operations, data quality checks and post modelling statistical checks. One
can effortlessly change class of a number of variables to factor, remove
duplicate observations from the data, create deciles of a variable,
perform data quality checks for continuous (integer or numeric),
categorical (factor) and date variables, and compute goodness of fit
measures such as auc for statistical models. The functions are consistent
for objects of class 'data.frame' and 'data.table', which is an enhanced
'data.frame' implemented in the package 'data.table'.

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
