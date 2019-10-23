%global packname  HSROC
%global packver   2.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.9
Release:          1%{?dist}
Summary:          Meta-Analysis of Diagnostic Test Accuracy when Reference Test isImperfect

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-MCMCpack 
Requires:         R-lattice 
Requires:         R-CRAN-coda 
Requires:         R-MASS 
Requires:         R-CRAN-MCMCpack 

%description
Implements a model for joint meta-analysis of sensitivity and specificity
of the diagnostic test under evaluation, while taking into account the
possibly imperfect sensitivity and specificity of the reference test. This
hierarchical model accounts for both within and between study variability.
Estimation is carried out using a Bayesian approach, implemented via a
Gibbs sampler. The model can be applied in situations where more than one
reference test is used in the selected studies.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
