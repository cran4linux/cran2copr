%global __brp_check_rpaths %{nil}
%global packname  BCBCSF
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bias-Corrected Bayesian Classification with Selected Features

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.1
Requires:         R-core >= 2.13.1
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-abind 

%description
Fully Bayesian Classification with a subset of high-dimensional features,
such as expression levels of genes. The data are modeled with a
hierarchical Bayesian models using heavy-tailed t distributions as priors.
When a large number of features are available, one may like to select only
a subset of features to use, typically those features strongly correlated
with the response in training cases. Such a feature selection procedure is
however invalid since the relationship between the response and the
features has be exaggerated by feature selection. This package provides a
way to avoid this bias and yield better-calibrated predictions for future
cases when one uses F-statistic to select features.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
