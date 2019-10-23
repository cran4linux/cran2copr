%global packname  QVM
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Questionnaires Validation Module

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ltm 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-gWidgets 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-IMPACT 
BuildRequires:    R-CRAN-multilevel 
Requires:         R-CRAN-ltm 
Requires:         R-tcltk 
Requires:         R-CRAN-gWidgets 
Requires:         R-CRAN-mvtnorm 
Requires:         R-nlme 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-IMPACT 
Requires:         R-CRAN-multilevel 

%description
Implement a multivariate analysis interface for questionnaire validation
of Likert-type scale variables.

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
