%global packname  AsyK
%global packver   1.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.4
Release:          2%{?dist}
Summary:          Kernel Density Estimation and Selection of Optimum Bandwidth

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-decon 
BuildRequires:    R-CRAN-kedd 
BuildRequires:    R-CRAN-locfit 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-kerdiest 
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-CRAN-ICV 
BuildRequires:    R-CRAN-OSCV 
Requires:         R-KernSmooth 
Requires:         R-CRAN-decon 
Requires:         R-CRAN-kedd 
Requires:         R-CRAN-locfit 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-kerdiest 
Requires:         R-CRAN-sm 
Requires:         R-CRAN-ICV 
Requires:         R-CRAN-OSCV 

%description
A collection of functions related to density estimation by using Chen's
(2000) idea. Mean Squared Errors (MSE) are calculated for estimated
curves. For this purpose, R functions allow the distribution to be Gamma,
Exponential or Weibull. For details see Chen (2000), Scaillet (2004)
<doi:10.1080/10485250310001624819> and Khan and Akbar.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
