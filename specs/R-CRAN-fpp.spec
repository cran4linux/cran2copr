%global packname  fpp
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          Data for "Forecasting: principles and practice"

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-fma 
BuildRequires:    R-CRAN-expsmooth 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-tseries 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-fma 
Requires:         R-CRAN-expsmooth 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-tseries 

%description
All data sets required for the examples and exercises in the book
"Forecasting: principles and practice" by Rob J Hyndman and George
Athanasopoulos. All packages required to run the examples are also loaded.

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
%{rlibdir}/%{packname}/INDEX
