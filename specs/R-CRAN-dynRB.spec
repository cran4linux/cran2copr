%global packname  dynRB
%global packver   0.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.15
Release:          3%{?dist}
Summary:          Dynamic Range Boxes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-vegan 
Requires:         R-foreign 
Requires:         R-CRAN-dplyr 

%description
Improves the concept of multivariate range boxes, which is highly
susceptible for outliers and does not consider the distribution of the
data. The package uses dynamic range boxes to overcome these problems.

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
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
