%global packname  GEint
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Misspecified Models for Gene-Environment Interaction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-bindata 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-speedglm 
BuildRequires:    R-CRAN-rje 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-bindata 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-speedglm 
Requires:         R-CRAN-rje 
Requires:         R-CRAN-geepack 
Requires:         R-stats 

%description
First major functionality is to compute the bias in misspecified linear
gene-environment interaction models. The most generalized function for
this objective is GE_bias().  However GE_bias() requires specification of
many higher order moments of covariates in the model.  If users are unsure
about how to calculate/estimate these higher order moments, it may be
easier to use GE_bias_normal_squaredmis().  This function places many more
assumptions on the covariates (most notably that they are all jointly
generated from a multivariate normal distribution) and is thus able to
automatically calculate many of the higher order moments automatically,
necessitating only that the user specify some covariances.  There are also
functions to solve for the bias through simulation and non-linear equation
solvers, these can be used to check your work. Second major functionality
is to implement the Bootstrap Inference with Correct Sandwich (BICS)
testing procedure, which we have found to provide better finite-sample
performance than other inference procedures for testing GxE interaction.
More details on these functions are available in Sun, Carroll, Christiani,
and Lin, "Testing for Gene-Environment Interaction Under Exposure
Misspecification" (In Revision).

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
