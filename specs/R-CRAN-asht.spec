%global packname  asht
%global packver   0.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          2%{?dist}
Summary:          Applied Statistical Hypothesis Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-exact2x2 
BuildRequires:    R-CRAN-exactci 
BuildRequires:    R-CRAN-bpcp 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-CRAN-perm 
BuildRequires:    R-CRAN-ssanv 
Requires:         R-stats 
Requires:         R-CRAN-exact2x2 
Requires:         R-CRAN-exactci 
Requires:         R-CRAN-bpcp 
Requires:         R-CRAN-coin 
Requires:         R-CRAN-perm 
Requires:         R-CRAN-ssanv 

%description
Gives some hypothesis test functions (sign test, median and other quantile
tests, Wilcoxon signed rank test, coefficient of variation test, test of
normal variance, test on weighted sums of Poisson [see Fay and Kim
<doi:10.1002/bimj.201600111>], sample size for t-tests with different
variances and non-equal n per arm, Behrens-Fisher test, nonparametric ABC
intervals, Wilcoxon-Mann-Whitney test [with effect estimates and
confidence intervals, see Fay and Malinovsky <doi:10.1002/sim.7890>],
two-sample melding tests [see Fay, Proschan, and Brittain
<doi:10.1111/biom.12231>], one-way ANOVA allowing var.equal=FALSE [see
Brown and Forsythe, 1974, Biometrics]). The focus is on methods that have
compatible confidence intervals.

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
