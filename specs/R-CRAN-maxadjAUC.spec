%global packname  maxadjAUC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Maximizing the Adjusted AUC

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-aucm 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-survival 
Requires:         R-CRAN-aucm 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-Hmisc 

%description
Fits a linear combination of predictors by maximizing a smooth
approximation to the estimated covariate-adjusted area under the receiver
operating characteristic curve (AUC) for a discrete covariate. (Meisner,
A, Parikh, CR, and Kerr, KF (2017)
<http://biostats.bepress.com/uwbiostat/paper421/>.)

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
