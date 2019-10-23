%global packname  MachineShop
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Machine Learning Models and Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-recipes >= 0.1.4
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-polspline 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-recipes >= 0.1.4
Requires:         R-CRAN-abind 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-party 
Requires:         R-CRAN-polspline 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-Rsolnp 
Requires:         R-survival 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Meta-package for statistical and machine learning with a unified interface
for model fitting, prediction, performance assessment, and presentation of
results.  Approaches for model fitting and prediction of numerical,
categorical, or censored time-to-event outcomes include traditional
regression models, regularization methods, tree-based methods, support
vector machines, neural networks, ensembles, data preprocessing,
filtering, and model tuning and selection.  Performance metrics are
provided for model assessment and can be estimated with independent test
sets, split sampling, cross-validation, or bootstrap resampling.  Resample
estimation can be executed in parallel for faster processing and nested in
cases of model tuning and selection.  Modeling results can be summarized
with descriptive statistics; calibration curves; variable importance;
partial dependence plots; confusion matrices; and ROC, lift, and other
performance curves.

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
