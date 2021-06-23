%global __brp_check_rpaths %{nil}
%global packname  harmonicmeanp
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Harmonic Mean p-Values and Model Averaging by Mean MaximumLikelihood

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-FMStable 
Requires:         R-CRAN-FMStable 

%description
The harmonic mean p-value (HMP) test combines p-values and corrects for
multiple testing while controlling the strong-sense family-wise error
rate. It is more powerful than common alternatives including Bonferroni
and Simes procedures when combining large proportions of all the p-values,
at the cost of slightly lower power when combining small proportions of
all the p-values. It is more stringent than controlling the false
discovery rate, and possesses theoretical robustness to positive
correlations between tests and unequal weights. It is a multi-level test
in the sense that a superset of one or more significant tests is certain
to be significant and conversely when the superset is non-significant, the
constituent tests are certain to be non-significant. It is based on MAMML
(model averaging by mean maximum likelihood), a frequentist analogue to
Bayesian model averaging, and is theoretically grounded in generalized
central limit theorem. For detailed examples type
vignette("harmonicmeanp") after installation. Version 3.0 addresses errors
in versions 1.0 and 2.0 that led function p.hmp to control the familywise
error rate only in the weak sense, rather than the strong sense as
intended.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
