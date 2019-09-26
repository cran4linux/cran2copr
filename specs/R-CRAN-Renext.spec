%global packname  Renext
%global packver   3.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}
Summary:          Renewal Method for Extreme Values Extrapolation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.8.0
Requires:         R-core >= 2.8.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-splines 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-numDeriv 
Requires:         R-splines 
Requires:         R-methods 

%description
Peaks Over Threshold (POT) or 'methode du renouvellement'. The
distribution for the exceedances can be chosen, and heterogeneous data
(including historical data or block data) can be used in a
Maximum-Likelihood framework.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/Rendata
%{rlibdir}/%{packname}/INDEX
