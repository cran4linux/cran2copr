%global packname  TAQMNGR
%global packver   2018.5-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2018.5.1
Release:          3%{?dist}
Summary:          Manage Tick-by-Tick Transaction Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    zlib-devel
Requires:         zlib
BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.0

%description
Manager of tick-by-tick transaction data that performs 'cleaning',
'aggregation' and 'import' in an efficient and fast way. The package
engine, written in C++, exploits the 'zlib' and 'gzstream' libraries to
handle gzipped data without need to uncompress them. 'Cleaning' and
'aggregation' are performed according to Brownlees and Gallo (2006)
<DOI:10.1016/j.csda.2006.09.030>. Currently, TAQMNGR processes raw data
from WRDS (Wharton Research Data Service,
<https://wrds-web.wharton.upenn.edu/wrds/>).

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
%{rlibdir}/%{packname}/libs
