%global packname  fitteR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Fit Hundreds of Theoretical Distributions to Empirical Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-tools 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-R.utils 
Requires:         R-tools 

%description
Systematic fit of hundreds of theoretical univariate distributions to
empirical data via maximum likelihood estimation. Fits are reported and
summarized by a data.frame, a csv file or a 'shiny' app (here with
additional features like visual representation of fits). All output
formats provide assessment of goodness-of-fit by the following methods:
Kolmogorov-Smirnov test, Shapiro-Wilks test, Anderson-Darling test.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
