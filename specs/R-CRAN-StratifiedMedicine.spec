%global packname  StratifiedMedicine
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Stratified Medicine

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggparty 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-ranger 
Requires:         R-survival 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggparty 
Requires:         R-CRAN-mvtnorm 

%description
A toolkit for stratified medicine, subgroup identification, and precision
medicine. Current tools include (1) filtering models (reduce covariate
space), (2) patient-level estimate models (counterfactual patient-level
quantities, for example the individual treatment effect), (3) subgroup
identification models (find subsets of patients with similar treatment
effects), and (4) parameter estimation and inference (for the overall
population and discovered subgroups). These tools can directly feed into
stratified medicine algorithms including PRISM (patient response
identifiers for stratified medicine; Jemielita and Mehrotra 2019
<arXiv:1912.03337>. PRISM is a flexible and general framework which
accepts user-created models/functions. This package is in beta and will be
continually updated.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
