%global packname  intercure
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Cure Rate Estimators for Interval Censored Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-survival 
BuildRequires:    R-MASS 
BuildRequires:    R-stats4 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-survival 
Requires:         R-MASS 
Requires:         R-stats4 
Requires:         R-Matrix 
Requires:         R-CRAN-iterators 
Requires:         R-parallel 

%description
Implementations of semiparametric cure rate estimators for interval
censored data in R. The algorithms are based on the promotion time and
frailty models, all for interval censoring. For the frailty model, there
is also a implementation contemplating clustered data.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
