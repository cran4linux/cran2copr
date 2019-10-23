%global packname  ordinalRR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Analysis of Repeatability and Reproducibility Studies withOrdinal Measurements

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags 
Requires:         R-CRAN-rjags 

%description
Implements Bayesian data analyses of balanced repeatability and
reproducibility studies with ordinal measurements. Model fitting is based
on MCMC posterior sampling with 'rjags'. Function ordinalRR() directly
carries out the model fitting, and this function has the flexibility to
allow the user to specify key aspects of the model, e.g., fixed versus
random effects. Functions for preprocessing data and for the numerical and
graphical display of a fitted model are also provided. There are also
functions for displaying the model at fixed (user-specified) parameters
and for simulating a hypothetical data set at a fixed (user-specified) set
of parameters for a random-effects rater population. For additional
technical details, refer to Culp, Ryan, Chen, and Hamada (2018) and cite
this Technometrics paper when referencing any aspect of this work. The
demo of this package reproduces results from the Technometrics paper.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
