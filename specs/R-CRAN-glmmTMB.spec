%global packname  glmmTMB
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Generalized Linear Mixed Models using Template Model Builder

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-TMB >= 1.7.14
BuildRequires:    R-CRAN-lme4 >= 1.1.18.9000
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-TMB >= 1.7.14
Requires:         R-CRAN-lme4 >= 1.1.18.9000
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-nlme 

%description
Fit linear and generalized linear mixed models with various extensions,
including zero-inflation. The models are fitted using maximum likelihood
estimation via 'TMB' (Template Model Builder). Random effects are assumed
to be Gaussian on the scale of the linear predictor and are integrated out
using the Laplace approximation. Gradients are calculated using automatic
differentiation.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/example_files
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/other_methods
%{rlibdir}/%{packname}/test_data
%{rlibdir}/%{packname}/vignette_data
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
