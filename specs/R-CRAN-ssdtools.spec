%global packname  ssdtools
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Species Sensitivity Distributions

License:          Apache License (== 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-chk 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-chk 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-VGAM 

%description
Species sensitivity distributions are cumulative probability distributions
which are fitted to toxicity concentrations for different species as
described by Posthuma et al.(2001) <isbn:9781566705783>. The ssdtools
package uses Maximum Likelihood to fit distributions such as the
log-normal, gamma, burr Type-III, log-logistic, log-Gumbel, Gompertz and
Weibull. The user can provide custom distributions. Multiple distributions
can be averaged using Information Criteria. Confidence intervals on hazard
concentrations and proportions are produced by parametric bootstrapping.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
