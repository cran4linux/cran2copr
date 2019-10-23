%global packname  tsqn
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Applications of the Qn Estimator to Time Series (Univariate andMultivariate)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-fracdiff 
Requires:         R-CRAN-robustbase 
Requires:         R-MASS 
Requires:         R-CRAN-fracdiff 

%description
Time Series Qn is a package with applications of the Qn estimator of
Rousseeuw and Croux (1993) <doi:10.1080/01621459.1993.10476408> to
univariate and multivariate Time Series in time and frequency domains.
More specifically, the robust estimation of autocorrelation or
autocovariance matrix functions from Ma and Genton (2000, 2001)
<doi:10.1111/1467-9892.00203>, <doi:10.1006/jmva.2000.1942> and Cotta
(2017) <doi:10.13140/RG.2.2.14092.10883> are provided. The robust
pseudo-periodogram of Molinares et. al. (2009)
<doi:10.1016/j.jspi.2008.12.014> is also given. This packages also
provides the M-estimator of the long-memory parameter d based on the
robustification of the GPH estimator proposed by Reisen et al. (2017)
<doi:10.1016/j.jspi.2017.02.008>.

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
