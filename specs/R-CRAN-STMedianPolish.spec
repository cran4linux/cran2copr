%global packname  STMedianPolish
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          3%{?dist}
Summary:          Spatio-Temporal Median Polish

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spacetime 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-nabor 
BuildRequires:    R-CRAN-gstat 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spacetime 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-nabor 
Requires:         R-CRAN-gstat 

%description
Analyses spatio-temporal data, decomposing data in n-dimensional arrays
and using the median polish technique.

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
%{rlibdir}/%{packname}/INDEX
