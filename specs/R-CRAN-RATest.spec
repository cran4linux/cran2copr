%global packname  RATest
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          3%{?dist}
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
version focuses on three testing problems and their implementation in
empirical work. First, it facilitates the empirical researcher to test for
particular hypotheses, such as comparisons of means, medians, and
variances from k populations using robust permutation tests, which
asymptotic validity holds under very weak assumptions, while retaining the
exact rejection probability in finite samples when the underlying
distributions are identical. Second, the description and implementation of
a permutation test for testing the continuity assumption of the baseline
covariates in the sharp regression discontinuity design (RDD) as in Canay
and Kamat (2017) <https://goo.gl/UZFqt7>. More specifically, it allows the
user to select a set of covariates and test the aforementioned hypothesis
using a permutation test based on the Cramer-von Miss test statistic.
Graphical inspection of the empirical CDF and histograms for the variables
of interest is also supported in the package. Third, it provides the
practitioner with an effortless implementation of a permutation test based
on the martingale decomposition of the empirical process for testing for
heterogeneous treatment effects in the presence of an estimated nuisance
parameter.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
