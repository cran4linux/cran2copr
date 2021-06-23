%global __brp_check_rpaths %{nil}
%global packname  StMoMo
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Stochastic Mortality Modelling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fields >= 8.2
BuildRequires:    R-CRAN-forecast >= 6.1
BuildRequires:    R-CRAN-fanplot >= 3.4
BuildRequires:    R-CRAN-rootSolve >= 1.6.1
BuildRequires:    R-CRAN-reshape2 >= 1.4.1
BuildRequires:    R-CRAN-gnm >= 1.0
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-fields >= 8.2
Requires:         R-CRAN-forecast >= 6.1
Requires:         R-CRAN-fanplot >= 3.4
Requires:         R-CRAN-rootSolve >= 1.6.1
Requires:         R-CRAN-reshape2 >= 1.4.1
Requires:         R-CRAN-gnm >= 1.0
Requires:         R-MASS 
Requires:         R-CRAN-RColorBrewer 

%description
Implementation of the family of generalised age-period-cohort stochastic
mortality models. This family of models encompasses many models proposed
in the actuarial and demographic literature including the Lee-Carter
(1992) <doi:10.2307/2290201> and the Cairns-Blake-Dowd (2006)
<doi:10.1111/j.1539-6975.2006.00195.x> models. It includes functions for
fitting mortality models, analysing their goodness-of-fit and performing
mortality projections and simulations.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
