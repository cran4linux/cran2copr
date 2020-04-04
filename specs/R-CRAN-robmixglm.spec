%global packname  robmixglm
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Robust Generalized Linear Models (GLM) using Mixtures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-bbmle 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-methods 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-CRAN-fastGHQuad 
Requires:         R-stats 
Requires:         R-CRAN-bbmle 
Requires:         R-MASS 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-actuar 
Requires:         R-methods 
Requires:         R-boot 
Requires:         R-CRAN-numDeriv 

%description
Robust generalized linear models (GLM) using a mixture method, as
described in Beath (2018) <doi:10.1080/02664763.2017.1414164>. This
assumes that the data are a mixture of standard observations, being a
generalised linear model, and outlier observations from an overdispersed
generalized linear model. The overdispersed linear model is obtained by
including a normally distributed random effect in the linear predictor of
the generalized linear model.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
