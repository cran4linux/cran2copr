%global packname  longRPart2
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          3%{?dist}
Summary:          Recursive Partitioning of Longitudinal Data

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-MASS 
Requires:         R-nlme 
Requires:         R-CRAN-ggplot2 
Requires:         R-rpart 
Requires:         R-CRAN-formula.tools 
Requires:         R-MASS 

%description
Performs recursive partitioning of linear and nonlinear mixed effects
models, specifically for longitudinal data. The package is an extension of
the original 'longRPart' package by Stewart and Abdolell (2013)
<https://cran.r-project.org/package=longRPart>.

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
