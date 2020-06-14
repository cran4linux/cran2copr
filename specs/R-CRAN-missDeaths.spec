%global packname  missDeaths
%global packver   2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6
Release:          2%{?dist}
Summary:          Simulating and Analyzing Time to Event Data in the Presence ofPopulation Mortality

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-relsurv 
BuildRequires:    R-CRAN-cmprsk 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mitools 
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-survival 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-relsurv 
Requires:         R-CRAN-cmprsk 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-mitools 

%description
Implements two methods: a nonparametric risk adjustment and a data
imputation method that use general population mortality tables to allow a
correct analysis of time to disease recurrence. Also includes a powerful
set of object oriented survival data simulation functions.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
