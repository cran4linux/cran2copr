%global packname  dendrometeR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Analyzing Dendrometer Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-pspline 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-methods 
Requires:         R-CRAN-forecast 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-pspline 
Requires:         R-stats 
Requires:         R-CRAN-zoo 
Requires:         R-methods 

%description
Various functions to import, verify, process and plot high-resolution
dendrometer using daily and stem-cycle approaches.

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
%doc %{rlibdir}/%{packname}/Changelog
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
