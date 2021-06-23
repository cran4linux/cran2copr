%global __brp_check_rpaths %{nil}
%global packname  glmvsd
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Variable Selection Deviation Measures and Instability Tests forHigh-Dimensional Generalized Linear Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-brglm 
Requires:         R-stats 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ncvreg 
Requires:         R-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-brglm 

%description
Variable selection deviation (VSD) measures and instability tests for
high-dimensional model selection methods such as LASSO, SCAD and MCP,
etc., to decide whether the sparse patterns identified by those methods
are reliable.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
