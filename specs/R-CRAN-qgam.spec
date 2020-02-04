%global packname  qgam
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          Smooth Additive Quantile Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-mgcv >= 1.8.28
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-grDevices 
Requires:         R-mgcv >= 1.8.28
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-grDevices 

%description
Smooth additive quantile regression models, fitted using the methods of
Fasiolo et al. (2017) <arXiv:1707.03307>. Differently from 'quantreg', the
smoothing parameters are estimated automatically by marginal loss
minimization, while the regression coefficients are estimated using either
PIRLS or Newton algorithm. The learning rate is determined so that the
Bayesian credible intervals of the estimated effects have approximately
the correct coverage. The main function is qgam() which is similar to
gam() in 'mgcv', but fits non-parametric quantile regression models.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
