%global packname  StVAR
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}
Summary:          Student's t Vector Autoregression (StVAR)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ADGofTest 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-matlab 
Requires:         R-CRAN-ADGofTest 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-matlab 

%description
Estimation of multivariate Student's t dynamic regression models for a
given degrees of freedom and lag length. Users can also specify the trends
and dummies of any kind in matrix form.

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
