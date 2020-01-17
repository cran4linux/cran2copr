%global packname  miWQS
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Multiple Imputation Using Weighted Quantile Sum Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.49
BuildRequires:    R-CRAN-Hmisc >= 4.1.1
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-survival >= 2.43.1
BuildRequires:    R-CRAN-glm2 >= 1.2.1
BuildRequires:    R-CRAN-Rsolnp >= 1.16
BuildRequires:    R-CRAN-invgamma >= 1.1
BuildRequires:    R-CRAN-truncnorm >= 1.0.8
BuildRequires:    R-CRAN-tidyr >= 0.8.2
BuildRequires:    R-CRAN-rlist >= 0.4.6.1
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-coda >= 0.19.2
BuildRequires:    R-CRAN-matrixNormal >= 0.0.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-MASS >= 7.3.49
Requires:         R-CRAN-Hmisc >= 4.1.1
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-survival >= 2.43.1
Requires:         R-CRAN-glm2 >= 1.2.1
Requires:         R-CRAN-Rsolnp >= 1.16
Requires:         R-CRAN-invgamma >= 1.1
Requires:         R-CRAN-truncnorm >= 1.0.8
Requires:         R-CRAN-tidyr >= 0.8.2
Requires:         R-CRAN-rlist >= 0.4.6.1
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-coda >= 0.19.2
Requires:         R-CRAN-matrixNormal >= 0.0.0
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
The `miWQS` package handles the uncertainty due to below the detection
limit in a correlated component mixture problem.  Researchers want to
determine if a set/mixture of continuous and correlated
components/chemicals is associated with an outcome and if so, which
components are important in that mixture. These components share a common
outcome but are interval-censored between zero and low thresholds, or
detection limits, that may be different across the components. The `miWQS`
package applies the multiple imputation (MI) procedure to the weighted
quantile sum regression (WQS) methodology for continuous, binary, or count
outcomes.  The imputation models are: bootstrapping imputation (Lubin
et.al (2004) <doi:10.1289/ehp.7199>) and Bayesian imputation.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
