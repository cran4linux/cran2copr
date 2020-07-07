%global packname  acfMPeriod
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Robust Estimation of the ACF from the M-Periodogram

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-MASS 
Requires:         R-MASS 

%description
Non-robust and robust computations of the sample autocovariance (ACOVF)
and sample autocorrelation functions (ACF) of univariate and multivariate
processes. The methodology consists in reversing the diagonalization
procedure involving the periodogram or the cross-periodogram and the
Fourier transform vectors, and, thus, obtaining the ACOVF or the ACF as
discussed in Fuller (1995) <doi:10.1002/9780470316917>. The robust version
is obtained by fitting robust M-regressors to obtain the M-periodogram or
M-cross-periodogram as discussed in Reisen et al. (2017)
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
