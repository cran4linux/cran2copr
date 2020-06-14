%global packname  BVS
%global packver   4.12.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.12.1
Release:          2%{?dist}
Summary:          Bayesian Variant Selection: Bayesian Model UncertaintyTechniques for Genetic Association Studies

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-haplo.stats 
Requires:         R-MASS 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-haplo.stats 

%description
The functions in this package focus on analyzing case-control association
studies involving a group of genetic variants.  In particular, we are
interested in modeling the outcome variable as a function of a
multivariate genetic profile using Bayesian model uncertainty and variable
selection techniques.  The package incorporates functions to analyze data
sets involving common variants as well as extensions to model rare
variants via the Bayesian Risk Index (BRI) as well as haplotypes.
Finally, the package also allows the incorporation of external biological
information to inform the marginal inclusion probabilities via the iBMU.

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
