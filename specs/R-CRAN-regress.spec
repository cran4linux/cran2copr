%global packname  regress
%global packver   1.3-15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.15
Release:          1%{?dist}
Summary:          Gaussian Linear Models with Linear Covariance Structure

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Functions to fit Gaussian linear model by maximising the residual log
likelihood where the covariance structure can be written as a linear
combination of known matrices.  Can be used for multivariate models and
random effects models.  Easy straight forward manner to specify random
effects models, including random interactions. Code now optimised to use
Sherman Morrison Woodbury identities for matrix inversion in random
effects models. We've added the ability to fit models using any kernel as
well as a function to return the mean and covariance of random effects
conditional on the data (BLUPs).

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
