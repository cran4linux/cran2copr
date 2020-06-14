%global packname  proportion
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          2%{?dist}
Summary:          Inference on Single Binomial Proportion and BayesianComputations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-TeachingDemos 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-TeachingDemos 
Requires:         R-CRAN-ggplot2 

%description
Abundant statistical literature has revealed the importance of
constructing and evaluating various methods for constructing confidence
intervals (CI) for single binomial proportion (p). We comprehensively
provide procedures in frequentist (approximate with or without adding
pseudo counts or continuity correction or exact) and in Bayesian cultures.
Evaluation procedures for CI warrant active computational attention and
required summaries pertaining to four criterion (coverage probability,
expected length, p-confidence, p-bias, and error) are implemented.

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
