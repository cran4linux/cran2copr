%global __brp_check_rpaths %{nil}
%global packname  understandBPMN
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Calculator of Understandability Metrics for BPMN

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-R.utils 
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-CRAN-XML 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-R.utils 

%description
Calculate several understandability metrics of BPMN models. BPMN stands
for business process modelling notation and is a language for expressing
business processes into business process diagrams. Examples of these
understandability metrics are: average connector degree, maximum connector
degree, sequentiality, cyclicity, diameter, depth, token split, control
flow complexity, connector mismatch, connector heterogeneity,
separability, structuredness and cross connectivity. See R documentation
and paper on metric implementation included in this package for more
information concerning the metrics.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
