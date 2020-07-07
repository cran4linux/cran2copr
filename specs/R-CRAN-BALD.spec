%global packname  BALD
%global packver   1.0.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.3
Release:          3%{?dist}
Summary:          Robust Loss Development Using MCMC

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    jags-devel >= 4.3.0
BuildRequires:    make
Requires:         jags
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-rjags >= 3.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-logspline 
BuildRequires:    R-utils 
BuildRequires:    R-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-rjags >= 3.3
Requires:         R-methods 
Requires:         R-CRAN-logspline 
Requires:         R-utils 
Requires:         R-lattice 
Requires:         R-stats 
Requires:         R-graphics 

%description
Bayesian analysis of loss development on insurance triangles or 'BALD' is
a Bayesian model of developing aggregate loss triangles in property
casualty insurance. This actuarial model makes use of a heteroskedastic
and skewed t-likelihood with endogenous degrees of freedom, employs model
averaging by means of Reversible Jump MCMC, and accommodates a structural
break in the path of the consumption of benefits. Further, the model is
capable of incorporating expert information in the calendar year effect.
In an accompanying vignette, this model is applied to two widely studied
General Liability and Auto Bodily Injury Liability loss triangles. For a
description of the methodology, see Frank A. Schmid (2010)
<doi:10.2139/ssrn.1501706>.

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
%doc %{rlibdir}/%{packname}/models
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
