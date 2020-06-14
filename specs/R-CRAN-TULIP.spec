%global packname  TULIP
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          A Toolbox for Linear Discriminant Analysis with Penalties

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildRequires:    R-CRAN-tensr 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-methods 
Requires:         R-CRAN-tensr 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-glmnet 
Requires:         R-methods 

%description
Integrates several popular high-dimensional methods based on Linear
Discriminant Analysis (LDA) and provides a comprehensive and user-friendly
toolbox for linear, semi-parametric and tensor-variate classification as
mentioned in Yuqing Pan, Qing Mai and Xin Zhang (2019) <arXiv:1904.03469>.
Functions are included for covariate adjustment, model fitting, cross
validation and prediction.

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
%{rlibdir}/%{packname}/libs
