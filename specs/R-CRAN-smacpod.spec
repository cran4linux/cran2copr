%global packname  smacpod
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          1%{?dist}
Summary:          Statistical Methods for the Analysis of Case-Control Point Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-sp 

%description
Statistical methods for analyzing case-control point data.  Methods
include the ratio of kernel densities, the difference in K Functions, the
spatial scan statistic, and q nearest neighbors of cases.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
