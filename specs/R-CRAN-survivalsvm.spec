%global packname  survivalsvm
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          2%{?dist}
Summary:          Survival Support Vector Analysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-survival 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-kernlab 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-Hmisc 

%description
Performs support vectors analysis for data sets with survival outcome.
Three approaches are available in the package: The regression approach
takes censoring into account when formulating the inequality constraints
of the support vector problem. In the ranking approach, the inequality
constraints set the objective to maximize the concordance index for
comparable pairs of observations. The hybrid approach combines the
regression and ranking constraints in the same model.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
