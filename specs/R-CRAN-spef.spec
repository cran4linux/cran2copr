%global packname  spef
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}
Summary:          Semiparametric Estimating Functions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-SQUAREM 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-nleqslv 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-SQUAREM 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-sm 
Requires:         R-survival 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-nleqslv 

%description
Functions for fitting semiparametric regression models for panel count
survival data. An overview of the package can be found in Wang and Yan
(2011) <doi:10.1016/j.cmpb.2010.10.005> and Chiou et al. (2018)
<doi:10.1111/insr.12271>.

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
%doc %{rlibdir}/%{packname}/bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
