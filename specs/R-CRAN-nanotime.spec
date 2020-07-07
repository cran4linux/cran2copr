%global packname  nanotime
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          3%{?dist}
Summary:          Nanosecond-Resolution Time for R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RcppCCTZ >= 0.2.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-RcppCCTZ >= 0.2.3
Requires:         R-methods 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-zoo 

%description
Full 64-bit resolution date and time support with resolution up to
nanosecond granularity is provided, with easy transition to and from the
standard 'POSIXct' type.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
