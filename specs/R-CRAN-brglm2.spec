%global debug_package %{nil}
%global packname  brglm2
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}
Summary:          Bias Reduction in Generalized Linear Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-graphics 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-enrichwith 
BuildRequires:    R-CRAN-lpSolveAPI 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-graphics 
Requires:         R-nnet 
Requires:         R-CRAN-enrichwith 
Requires:         R-CRAN-lpSolveAPI 
Requires:         R-CRAN-numDeriv 

%description
Estimation and inference from generalized linear models based on various
methods for bias reduction and maximum penalized likelihood with powers of
the Jeffreys prior as penalty. The 'brglmFit' fitting method can achieve
reduction of estimation bias by solving either the mean bias-reducing
adjusted score equations in Firth (1993) <doi:10.1093/biomet/80.1.27> and
Kosmidis and Firth (2009) <doi:10.1093/biomet/asp055>, or the median
bias-reduction adjusted score equations in Kenne et al. (2016)
<arXiv:1604.04768>, or through the direct subtraction of an estimate of
the bias of the maximum likelihood estimator from the maximum likelihood
estimates as in Cordeiro and McCullagh (1991)
<http://www.jstor.org/stable/2345592>. See Kosmidis et al (2019)
<doi:10.1007/s11222-019-09860-6> for more details. Estimation in all cases
takes place via a quasi Fisher scoring algorithm, and S3 methods for the
construction of of confidence intervals for the reduced-bias estimates are
provided. In the special case of generalized linear models for binomial
and multinomial responses (both ordinal and nominal), the adjusted score
approaches return estimates with improved frequentist properties, that are
also always finite, even in cases where the maximum likelihood estimates
are infinite (e.g. complete and quasi-complete separation). 'brglm2' also
provides pre-fit and post-fit methods for detecting separation and
infinite maximum likelihood estimates in binomial response generalized
linear models.

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
%doc %{rlibdir}/%{packname}/empir_tests.R
%doc %{rlibdir}/%{packname}/empirical_br_tests.R
%{rlibdir}/%{packname}/INDEX
