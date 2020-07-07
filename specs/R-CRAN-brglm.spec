%global packname  brglm
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          3%{?dist}
Summary:          Bias Reduction in Binomial-Response Generalized Linear Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildRequires:    R-CRAN-profileModel 
Requires:         R-CRAN-profileModel 

%description
Fit generalized linear models with binomial responses using either an
adjusted-score approach to bias reduction or maximum penalized likelihood
where penalization is by Jeffreys invariant prior. These procedures return
estimates with improved frequentist properties (bias, mean squared error)
that are always finite even in cases where the maximum likelihood
estimates are infinite (data separation). Fitting takes place by fitting
generalized linear models on iteratively updated pseudo-data. The
interface is essentially the same as 'glm'.  More flexibility is provided
by the fact that custom pseudo-data representations can be specified and
used for model fitting. Functions are provided for the construction of
confidence intervals for the reduced-bias estimates.

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
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
