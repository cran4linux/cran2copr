%global packname  cocoreg
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Extract Shared Variation in Collections of Data Sets UsingRegression Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-CCAGFA 
BuildRequires:    R-CRAN-RGCCA 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-multiway 
BuildRequires:    R-CRAN-reshape 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-CCAGFA 
Requires:         R-CRAN-RGCCA 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-abind 
Requires:         R-MASS 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-multiway 
Requires:         R-CRAN-reshape 

%description
The algorithm extracts shared variation from a collection of data sets
using regression models.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
