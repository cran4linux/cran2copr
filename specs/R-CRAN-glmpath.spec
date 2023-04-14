%global __brp_check_rpaths %{nil}
%global packname  glmpath
%global packver   0.98
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.98
Release:          3%{?dist}%{?buildtag}
Summary:          L1 Regularization Path for Generalized Linear Models and CoxProportional Hazards Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0
Requires:         R-core >= 2.0
BuildRequires:    R-survival 
Requires:         R-survival 

%description
A path-following algorithm for L1 regularized generalized linear models
and Cox proportional hazards model.

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
