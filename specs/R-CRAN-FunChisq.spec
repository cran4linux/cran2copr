%global packname  FunChisq
%global packver   2.4.5-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.5.3
Release:          1%{?dist}
Summary:          Chi-Square and Exact Tests for Model-Free Functional Dependency

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Statistical hypothesis testing methods for model-free functional
dependency using asymptotic chi-square or exact distributions. Functional
chi-squares are asymmetric and functionally optimal, unique from other
related statistics. Tests in this package reveal evidence for causality
based on the causality-by-functionality principle. They include asymptotic
functional chi-square tests, an exact functional test, a comparative
functional chi-square test, and also a comparative chi-square test. The
normalized non-constant functional chi-square test was used by Best
Performer NMSUSongLab in HPN-DREAM (DREAM8) Breast Cancer Network
Inference Challenges. A function index derived from the functional
chi-square offers a new effect size measure for the strength of function
dependency, a better alternative to conditional entropy in many aspects.
For continuous data, these tests offer an advantage over regression
analysis when a parametric functional form cannot be assumed; for
categorical data, they provide a novel means to assess directional
dependency not possible with symmetrical Pearson's chi-square or Fisher's
exact tests.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
