%global packname  VARsignR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Sign Restrictions, Bayesian, Vector Autoregression Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-HI 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-HI 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-mvnfast 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Provides routines for identifying structural shocks in vector
autoregressions (VARs) using sign restrictions.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
