%global __brp_check_rpaths %{nil}
%global packname  RSAlgaeR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Builds Empirical Remote Sensing Models of Water QualityVariables and Analyzes Long-Term Trends

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-hydroGOF 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cvTools 
BuildRequires:    R-CRAN-mblm 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-hydroGOF 
Requires:         R-stats 
Requires:         R-CRAN-cvTools 
Requires:         R-CRAN-mblm 
Requires:         R-graphics 
Requires:         R-utils 

%description
Assists in processing reflectance data, developing empirical models using
stepwise regression and a generalized linear modeling approach, cross-
validation, and analysis of trends in water quality conditions
(specifically chl-a) and climate conditions using the Theil-Sen estimator.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
