%global debug_package %{nil}
%global packname  jmdl
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Joint Mean-Correlation Regression Approach for DiscreteLongitudinal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-Formula 
Requires:         R-methods 
Requires:         R-CRAN-minqa 
Requires:         R-boot 
Requires:         R-CRAN-mnormt 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 

%description
Fit joint mean-correlation models for discrete longitudinal data (Tang
CY,Zhang W, Leng C, 2017 <doi:10.5705/ss.202016.0435>).

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
%{rlibdir}/%{packname}/INDEX
