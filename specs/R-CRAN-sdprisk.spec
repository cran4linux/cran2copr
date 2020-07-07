%global packname  sdprisk
%global packver   1.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          3%{?dist}
Summary:          Measures of Risk for the Compound Poisson Risk Process withDiffusion

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-PolynomF >= 2.0.0
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-PolynomF >= 2.0.0
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-rootSolve 
Requires:         R-utils 
Requires:         R-stats 

%description
Based on the compound Poisson risk process that is perturbed by a Brownian
motion, saddlepoint approximations to some measures of risk are provided.
Various approximation methods for the probability of ruin are also
included. Furthermore, exact values of both the risk measures as well as
the probability of ruin are available if the individual claims follow a
hypo-exponential distribution (i. e., if it can be represented as a sum of
independent exponentially distributed random variables with different rate
parameters). For more details see Gatto and Baumgartner (2014)
<doi:10.1007/s11009-012-9316-5>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
