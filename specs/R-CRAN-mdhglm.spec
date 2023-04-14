%global __brp_check_rpaths %{nil}
%global packname  mdhglm
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          3%{?dist}%{?buildtag}
Summary:          Multivariate Double Hierarchical Generalized Linear Models

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-boot 
Requires:         R-CRAN-mvtnorm 

%description
Allows various models for multivariate response variables where each
response is assumed to follow double hierarchical generalized linear
models. In double hierarchical generalized linear models, the mean,
dispersion parameters for variance of random effects, and residual
variance can be further modeled as random-effect models.

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
