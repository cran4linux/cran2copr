%global packname  MomTrunc
%global packver   4.59
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.59
Release:          1%{?dist}
Summary:          Moments of Folded and Doubly Truncated MultivariateDistributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-mvtnorm 

%description
It computes the raw moments for the truncated and folded multivariate
normal, Skew-normal (SN), Extended skew normal (ESN) and Student's
t-distribution. It also offers specific functions to compute the mean and
variance-covariance matrix as well as the cumulative distribution function
(cdf) for the folded normal, SN, ESN, and folded t-distribution. Density
and random deviates are offered for the ESN (SN as particular case)
distribution. Most algorithms are extensions based on Kan, R., & Robotti,
C. (2017) <doi:10.1080/10618600.2017.1322092>.

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
