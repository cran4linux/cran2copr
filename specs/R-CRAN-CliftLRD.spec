%global __brp_check_rpaths %{nil}
%global packname  CliftLRD
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Complex-Valued Wavelet Lifting Estimators of the Hurst Exponentfor Irregularly Sampled Time Series

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CNLTreg 
BuildRequires:    R-CRAN-liftLRD 
Requires:         R-CRAN-CNLTreg 
Requires:         R-CRAN-liftLRD 

%description
Implementation of Hurst exponent estimators based on complex-valued
lifting wavelet energy from Knight, M. I and Nunes, M. A. (2018)
<doi:10.1007/s11222-018-9820-8>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
