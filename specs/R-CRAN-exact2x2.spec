%global packname  exact2x2
%global packver   1.6.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.3.1
Release:          2%{?dist}
Summary:          Exact Tests and Confidence Intervals for 2x2 Tables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats >= 3.1.1
BuildRequires:    R-CRAN-exactci 
BuildRequires:    R-CRAN-ssanv 
Requires:         R-stats >= 3.1.1
Requires:         R-CRAN-exactci 
Requires:         R-CRAN-ssanv 

%description
Calculates conditional exact tests (Fisher's exact test, Blaker's exact
test, or exact McNemar's test) and unconditional exact tests (including
score-based tests on differences in proportions, ratios of proportions,
and odds ratios, and Boshcloo's test) with appropriate matching confidence
intervals, and provides power and sample size calculations. Gives melded
confidence intervals for the binomial case. Gives boundary-optimized
rejection region test (Gabriel, et al, 2018, <DOI:10.1002/sim.7579>), an
unconditional exact test for the situation where the controls are all
expected to fail.

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
%doc %{rlibdir}/%{packname}/slowTests
%{rlibdir}/%{packname}/INDEX
