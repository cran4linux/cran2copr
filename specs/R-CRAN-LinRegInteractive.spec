%global packname  LinRegInteractive
%global packver   0.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Interactive Interpretation of Linear Regression Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rpanel >= 1.1.3
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-rpanel >= 1.1.3
Requires:         R-CRAN-xtable 

%description
Interactive visualization of effects, response functions and marginal
effects for different kinds of regression models. In this version linear
regression models, generalized linear models, generalized additive models
and linear mixed-effects models are supported. Major features are the
interactive approach and the handling of the effects of categorical
covariates: if two or more factors are used as covariates every
combination of the levels of each factor is treated separately. The
automatic calculation of marginal effects and a number of possibilities to
customize the graphical output are useful features as well.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
