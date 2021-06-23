%global __brp_check_rpaths %{nil}
%global packname  RATest
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Randomization Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00
Requires:         R-core >= 3.00
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quantreg 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-gridExtra 
Requires:         R-stats 
Requires:         R-CRAN-quantreg 

%description
A collection of randomization tests, data sets and examples. The current
version focuses on four testing problems and their implementation in
empirical work. First, it facilitates the empirical researcher to test for
particular hypotheses, such as comparisons of means, medians, and
variances from k populations using robust permutation tests, which
asymptotic validity holds under very weak assumptions, while retaining the
exact rejection probability in finite samples when the underlying
distributions are identical. Second, the description and implementation of
a permutation test for testing the continuity assumption of the baseline
covariates in the sharp regression discontinuity design (RDD) as in Canay
and Kamat (2018) <https://goo.gl/UZFqt7>. More specifically, it allows the
user to select a set of covariates and test the aforementioned hypothesis
using a permutation test based on the Cramer-von Miss test statistic.
Graphical inspection of the empirical CDF and histograms for the variables
of interest is also supported in the package. Third, it provides the
practitioner with an effortless implementation of a permutation test based
on the martingale decomposition of the empirical process for testing for
heterogeneous treatment effects in the presence of an estimated nuisance
parameter as in Chung and Olivares (2020) <https://rb.gy/dwbbyx>. Lastly,
this version considers the two-sample goodness-of-fit testing problem
under covariate adaptive randomization and implements a permutation test
based on a prepivoted Kolmogorov-Smirnov test statistic.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
