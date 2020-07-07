%global packname  regmedint
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Regression-Based Causal Mediation Analysis with an InteractionTerm

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-survival 
Requires:         R-CRAN-Deriv 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-sandwich 
Requires:         R-survival 

%description
'R' re-implementation of the regression-based causal mediation analysis
with a treatment-mediator interaction term, as originally implemented in
the 'SAS' macro by Valeri and VanderWeele (2013) <doi:10.1037/a0031034>
and Valeri and VanderWeele (2015) <doi:10.1097/EDE.0000000000000253>.
Linear and logistic models are supported for the mediator model. Linear,
logistic, loglinear, Poisson, negative binomial, Cox, and accelerated
failure time (exponential and Weibull) models are supported for the
outcome model.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
