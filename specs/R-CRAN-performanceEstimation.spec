%global packname  performanceEstimation
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          An Infra-Structure for Performance Estimation of PredictiveModels

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-parallelMap >= 1.3
BuildRequires:    R-CRAN-ggplot2 >= 0.9.3
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-CRAN-tidyr >= 0.4.1
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-parallelMap >= 1.3
Requires:         R-CRAN-ggplot2 >= 0.9.3
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-CRAN-tidyr >= 0.4.1
Requires:         R-methods 
Requires:         R-parallel 

%description
An infra-structure for estimating the predictive performance of predictive
models. In this context, it can also be used to compare and/or select
among different alternative ways of solving one or more predictive tasks.
The main goal of the package is to provide a generic infra-structure to
estimate the values of different metrics of predictive performance using
different estimation procedures. These estimation tasks can be applied to
any solutions (workflows) to the predictive tasks. The package provides
easy to use standard workflows that allow the usage of any available R
modeling algorithm together with some pre-defined data pre-processing
steps and also prediction post- processing methods. It also provides means
for addressing issues related with the statistical significance of the
observed differences.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
