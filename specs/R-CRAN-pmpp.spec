%global packname  pmpp
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Posterior Mean Panel Predictor

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-pracma 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 

%description
Dynamic panel modelling framework based on an empirical-Bayes approach.
Contains tools for computing point forecasts and bootstrapping prediction
intervals. Reference: Liu et al. (2016) <doi:10.2139/ssrn.2889000>.

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
