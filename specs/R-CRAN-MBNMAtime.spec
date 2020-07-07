%global packname  MBNMAtime
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}
Summary:          Run Time-Course MBNMA Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.8
BuildRequires:    R-CRAN-checkmate >= 1.8.5
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-R2jags >= 0.5.7
BuildRequires:    R-CRAN-Rdpack >= 0.10.1
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-rjags >= 4.8
Requires:         R-CRAN-checkmate >= 1.8.5
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-R2jags >= 0.5.7
Requires:         R-CRAN-Rdpack >= 0.10.1
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Fits Bayesian time-course models for model-based network meta-analysis
(MBNMA) and model-based meta -analysis (MBMA) that account for repeated
measures over time within studies by applying different time-course
functions, following the method of Pedder et al. (2019)
<doi:10.1002/jrsm.1351>. The method allows synthesis of studies with
multiple follow-up measurements that can account for time-course for a
single or multiple treatment comparisons. Several general time-course
functions are provided; others may be added by the user. Various
characteristics can be flexibly added to the models, such as correlation
between time points and shared class effects. The consistency of direct
and indirect evidence in the network can be assessed using unrelated mean
effects models and/or by node-splitting.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
