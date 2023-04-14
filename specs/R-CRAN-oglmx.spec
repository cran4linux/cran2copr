%global __brp_check_rpaths %{nil}
%global packname  oglmx
%global packver   3.0.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Estimation of Ordered Generalized Linear Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-stats 
Requires:         R-CRAN-maxLik 
Requires:         R-stats 

%description
Ordered models such as ordered probit and ordered logit presume that the
error variance is constant across observations. In the case that this
assumption does not hold estimates of marginal effects are typically
biased (Weiss (1997)). This package allows for generalization of ordered
probit and ordered logit models by allowing the user to specify a model
for the variance. Furthermore, the package includes functions to calculate
the marginal effects. Wrapper functions to estimate the standard limited
dependent variable models are also included.

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
