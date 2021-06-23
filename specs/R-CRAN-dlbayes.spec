%global __brp_check_rpaths %{nil}
%global packname  dlbayes
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Use Dirichlet Laplace Prior to Solve Linear Regression Problemand Do Variable Selection

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-GIGrvg 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-glmnet 
Requires:         R-MASS 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-stats 
Requires:         R-graphics 

%description
The Dirichlet Laplace shrinkage prior in Bayesian linear regression and
variable selection, featuring: utility functions in implementing
Dirichlet-Laplace priors such as visualization; scalability in Bayesian
linear regression; penalized credible regions for variable selection.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
