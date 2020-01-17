%global packname  Ball
%global packver   1.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.9
Release:          1%{?dist}
Summary:          Statistical Inference and Sure Independence Screening via BallStatistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-utils 
Requires:         R-CRAN-gam 
Requires:         R-survival 
Requires:         R-CRAN-mvtnorm 

%description
Hypothesis tests and sure independence screening (SIS) procedure based on
ball statistics, including ball divergence <doi:10.1214/17-AOS1579>, ball
covariance <doi:10.1080/01621459.2018.1543600>, and ball correlation
<doi:10.1080/01621459.2018.1462709>, are developed to analyze complex data
in metric spaces, e.g, shape, directional, compositional and symmetric
positive definite matrix data. The ball divergence and ball covariance
based distribution-free tests are implemented to detecting distribution
difference and association in metric spaces <arXiv:1811.03750>.
Furthermore, several generic non-parametric feature selection procedures
based on ball correlation, BCor-SIS and all of its variants, are
implemented to tackle the challenge in the context of ultra high
dimensional data.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
