%global packname  RLRsim
%global packver   3.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.6
Release:          3%{?dist}
Summary:          Exact (Restricted) Likelihood Ratio Tests for Mixed and AdditiveModels

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-lme4 >= 1.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-mgcv 
BuildRequires:    R-nlme 
Requires:         R-CRAN-lme4 >= 1.1
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-mgcv 
Requires:         R-nlme 

%description
Rapid, simulation-based exact (restricted) likelihood ratio tests for
testing the presence of variance components/nonparametric terms for models
fit with nlme::lme(),lme4::lmer(), lmeTest::lmer(), gamm4::gamm4(),
mgcv::gamm() and SemiPar::spm().

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
