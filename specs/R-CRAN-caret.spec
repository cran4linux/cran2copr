%global packname  caret
%global packver   6.0-84
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.84
Release:          1%{?dist}
Summary:          Classification and Regression Training

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-withr >= 2.0.0
BuildRequires:    R-CRAN-ModelMetrics >= 1.1.0
BuildRequires:    R-lattice >= 0.20
BuildRequires:    R-CRAN-recipes >= 0.1.4
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-withr >= 2.0.0
Requires:         R-CRAN-ModelMetrics >= 1.1.0
Requires:         R-lattice >= 0.20
Requires:         R-CRAN-recipes >= 0.1.4
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-nlme 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Misc functions for training and plotting classification and regression
models.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/models
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
