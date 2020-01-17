%global packname  AsyK
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}
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
Density estimation by using symmetrical kernels and to calculate mean
square error. See Scaillet (2004) <doi:10.1080/10485250310001624819> and
Khan and Akbar (2019).

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
