%global packname  conover.test
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          3%{?dist}
Summary:          Conover-Iman Test of Multiple Comparisons Using Rank Sums

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Computes the Conover-Iman test (1979) for stochastic dominance and reports
the results among multiple pairwise comparisons after a Kruskal-Wallis
test for stochastic dominance among k groups (Kruskal and Wallis, 1952).
The interpretation of stochastic dominance requires an assumption that the
CDF of one group does not cross the CDF of the other. conover.test makes
k(k-1)/2 multiple pairwise comparisons based on Conover-Iman
t-test-statistic of the rank differences. The null hypothesis for each
pairwise comparison is that the probability of observing a randomly
selected value from the first group that is larger than a randomly
selected value from the second group equals one half; this null hypothesis
corresponds to that of the Wilcoxon-Mann-Whitney rank-sum test. Like the
rank-sum test, if the data can be assumed to be continuous, and the
distributions are assumed identical except for a difference in location,
Conover-Iman test may be understood as a test for median difference.
conover.test accounts for tied ranks. The Conover-Iman test is strictly
valid if and only if the corresponding Kruskal-Wallis null hypothesis is
rejected.

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
