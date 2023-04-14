%global __brp_check_rpaths %{nil}
%global packname  BayesMixSurv
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Mixture Survival Models using AdditiveMixture-of-Weibull Hazards, with Lasso Shrinkage andStratification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival 
Requires:         R-survival 

%description
Bayesian Mixture Survival Models using Additive Mixture-of-Weibull
Hazards, with Lasso Shrinkage and Stratification. As a Bayesian dynamic
survival model, it relaxes the proportional-hazard assumption. Lasso
shrinkage controls overfitting, given the increase in the number of free
parameters in the model due to presence of two Weibull components in the
hazard function.

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
