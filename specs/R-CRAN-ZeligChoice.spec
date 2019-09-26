%global packname  ZeligChoice
%global packver   0.9-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6
Release:          1%{?dist}
Summary:          Zelig Choice Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Zelig >= 5.1.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-Zelig >= 5.1.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-jsonlite 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-VGAM 

%description
Add-on package for Zelig 5. Enables the use of a variety of logit and
probit regressions.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/JSON
%{rlibdir}/%{packname}/INDEX
