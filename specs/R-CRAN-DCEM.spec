%global packname  DCEM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Clustering for Multivariate and Univariate Data UsingExpectation Maximization Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.49
BuildRequires:    R-CRAN-mvtnorm >= 1.0.7
BuildRequires:    R-CRAN-matrixcalc >= 1.0.3
Requires:         R-MASS >= 7.3.49
Requires:         R-CRAN-mvtnorm >= 1.0.7
Requires:         R-CRAN-matrixcalc >= 1.0.3

%description
Implements the Expectation Maximisation (EM)/(EM*) algorithm for
clustering finite gaussian mixture models for both multivariate and
univariate datasets. The initialization is done by randomly selecting the
samples from the dataset as the mean of the Gaussian(s). This version
implements the faster alternative EM* that avoids revisiting data by
leveraging the heap structure. The algorithm returns a set of Gaussian
parameters-posterior probabilities, mean, co-variance matrices
(multivariate data)/standard-deviation (for univariate datasets) and
priors. Reference: Hasan Kurban, Mark Jenne, Mehmet M. Dalkilic (2016)
<doi:10.1007/s41060-017-0062-1>. This work is partially supported by NCI
Grant 1R01CA213466-01.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
