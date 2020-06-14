%global packname  dtp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Dynamic Panel Threshold Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-plyr 

%description
Compute the dynamic threshold panel model suggested by (Stephanie Kremer,
Alexander Bick and Dieter Nautz (2013) <doi:10.1007/s00181-012-0553-9>) in
which they extended the (Hansen (1999) <doi:
10.1016/S0304-4076(99)00025-1>) original static panel threshold estimation
and the Caner and (Hansen (2004) <doi:10.1017/S0266466604205011>)
cross-sectional instrumental variable threshold model, where generalized
methods of moments type estimators are used.

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
