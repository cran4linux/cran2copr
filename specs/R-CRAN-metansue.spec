%global packname  metansue
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          1%{?dist}
Summary:          Meta-Analysis of Studies with Non-Statistically SignificantUnreported Effects

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Novel method to unbiasedly include studies with Non-statistically
Significant Unreported Effects (NSUEs) in a meta-analysis
<doi:10.1001/jamapsychiatry.2015.2196> and <doi:10.1177/0962280218811349>.
Briefly, the method first calculates the interval where the unreported
effects (e.g. t-values) should be according to the threshold of
statistical significance used in each study. Afterwards, maximum
likelihood techniques are used to impute the expected effect size of each
study with NSUEs, accounting for between-study heterogeneity and potential
covariates. Multiple imputations of the NSUEs are then randomly created
based on the expected value, variance and statistical significance bounds.
Finally, a restricted-maximum likelihood random-effects meta-analysis is
separately conducted for each set of imputations, and estimations from
these meta-analyses are pooled. Please read the reference in 'metansue'
for details of the procedure.

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
%{rlibdir}/%{packname}/INDEX
