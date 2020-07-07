%global packname  DELTD
%global packver   2.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.5
Release:          3%{?dist}
Summary:          Kernel Density Estimation using Lifetime Distributions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
A collection of asymmetrical kernels belong to lifetime distributions for
kernel density estimation is presented. Mean Squared Errors (MSE) are
calculated for estimated curves. For this purpose, R functions allow the
distribution to be Gamma, Exponential or Weibull. For details see Chen
(2000), Jin and Kawczak (2003) and Salha et al. (2014)
<doi:10.12988/pms.2014.4616>.

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
