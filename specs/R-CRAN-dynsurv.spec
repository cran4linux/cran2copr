%global packname  dynsurv
%global packver   0.3-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7
Release:          3%{?dist}
Summary:          Dynamic Models for Survival Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-BH >= 1.54.0.2
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-stats 
BuildRequires:    R-survival 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape 
Requires:         R-stats 
Requires:         R-survival 
Requires:         R-utils 

%description
Time-varying coefficient models for interval censored and right censored
survival data including 1) Bayesian Cox model with time-independent,
time-varying or dynamic coefficients for right censored and interval
censored data studied by Sinha et al. (1999)
<doi:10.1111/j.0006-341X.1999.00585.x> and Wang et al. (2013)
<doi:10.1007/s10985-013-9246-8>, 2) Spline based time-varying coefficient
Cox model for right censored data proposed by Perperoglou et al. (2006)
<doi:10.1016/j.cmpb.2005.11.006>, and 3) Transformation model with
time-varying coefficients for right censored data using estimating
equations proposed by Peng and Huang (2007) <doi:10.1093/biomet/asm058>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
