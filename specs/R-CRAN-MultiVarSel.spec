%global packname  MultiVarSel
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Variable Selection in a Multivariate Linear Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix >= 1.2.11
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-parallel 
Requires:         R-Matrix >= 1.2.11
Requires:         R-CRAN-glmnet 
Requires:         R-parallel 

%description
It performs variable selection in a multivariate linear model by
estimating the covariance matrix of the residuals then use it to remove
the dependence that may exist among the responses and eventually performs
variable selection by using the Lasso criterion. The method is described
in the paper Perrot-Dockès et al. (2017) <arXiv:1704.00076>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
