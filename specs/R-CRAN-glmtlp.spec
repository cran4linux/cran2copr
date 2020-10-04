%global packname  glmtlp
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Truncated Lasso Regularized Generalized Linear Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-glmnet 

%description
It provides an extremely efficient procedure for fitting the entire
truncated lasso regularization path for linear regression, logistic and
multinomial regression models, Poisson regression and the Cox model. The
algorithm uses the difference of convex technique. The detail of the
algorithm is described in Shen, Pan and Zhu (2012)
<doi:10.1080/01621459.2011.645783>. The package is inherited from a
popular R package 'glmnet' and many functions in 'glmnet' can be directly
used in 'glmtlp'. You can learn more details by the online manual
(<http://wuchong.org/glmtlp.html>).

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
