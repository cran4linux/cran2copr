%global packname  cit
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          4%{?dist}%{?buildtag}
Summary:          Causal Inference Test

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
Requires:         gsl
BuildRequires:    R-devel
Requires:         R-core

%description
A likelihood-based hypothesis testing approach is implemented for
assessing causal mediation. For example, it could be used to test for
mediation of a known causal association between a DNA variant, the
'instrumental variable', and a clinical outcome or phenotype by gene
expression or DNA methylation, the potential mediator. Another example
would be testing mediation of the effect of a drug on a clinical outcome
by the molecular target. The hypothesis test generates a p-value or
permutation-based FDR value with confidence intervals to quantify
uncertainty in the causal inference. The outcome can be represented by
either a continuous or binary variable, the potential mediator is
continuous, and the instrumental variable can be continuous or binary and
is not limited to a single variable but may be a design matrix
representing multiple variables.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
