%global packname  catch
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Covariate-Adjusted Tensor Classification in High-Dimensions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildRequires:    R-CRAN-tensr 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
Requires:         R-CRAN-tensr 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-methods 

%description
Performs classification and variable selection on high-dimensional tensors
(multi-dimensional arrays) after adjusting for additional covariates
(scalar or vectors) as CATCH model in Pan, Mai and Zhang (2018)
<arXiv:1805.04421>. The low-dimensional covariates and the
high-dimensional tensors are jointly modeled to predict a categorical
outcome in a multi-class discriminant analysis setting. The
Covariate-Adjusted Tensor Classification in High-dimensions (CATCH) model
is fitted in two steps: (1) adjust for the covariates within each class;
and (2) penalized estimation with the adjusted tensor using a cyclic block
coordinate descent algorithm. The package can provide a solution path for
tuning parameter in the penalized estimation step. Special case of the
CATCH model includes linear discriminant analysis model and matrix (or
tensor) discriminant analysis without covariates.

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
