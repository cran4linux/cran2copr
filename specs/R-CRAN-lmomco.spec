%global packname  lmomco
%global packver   2.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.2
Release:          1%{?dist}
Summary:          L-Moments, Censored L-Moments, Trimmed L-Moments, L-Comoments,and Many Distributions

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-goftest 
BuildRequires:    R-CRAN-Lmoments 
BuildRequires:    R-MASS 
Requires:         R-utils 
Requires:         R-CRAN-goftest 
Requires:         R-CRAN-Lmoments 
Requires:         R-MASS 

%description
Extensive functions for L-moments (LMs) and probability-weighted moments
(PWMs), parameter estimation for distributions, LM computation for
distributions, and L-moment ratio diagrams. Maximum likelihood and maximum
product of spacings estimation are also available. LMs for right-tail and
left-tail censoring by known or unknown threshold and by indicator
variable are available. Asymmetric (asy) trimmed LMs (TL-moments, TLMs)
are supported. LMs of residual (resid) and reversed (rev) resid life are
implemented along with 13 quantile function operators for reliability and
survival analyses. Exact analytical bootstrap estimates of order
statistics, LMs, and variances- covariances of LMs are provided. The
Harri-Coble Tau34-squared Normality Test is available. Distribution
support with "L" (LMs), "TL" (TLMs) and added (+) support for right-tail
censoring (RC) encompasses: Asy Exponential (Exp) Power [L], Asy
Triangular [L], Cauchy [TL], Eta-Mu [L], Exp. [L], Gamma [L], Generalized
(Gen) Exp Poisson [L], Gen Extreme Value [L], Gen Lambda [L,TL], Gen
Logistic [L), Gen Normal [L], Gen Pareto [L+RC, TL], Govindarajulu [L],
Gumbel [L], Kappa [L], Kappa-Mu [L], Kumaraswamy [L], Laplace [L], Linear
Mean Resid. Quantile Function [L], Normal [L], 3-p log-Normal [L], Pearson
Type III [L], Rayleigh [L], Rev-Gumbel [L+RC], Rice/Rician [L], Slash
[TL], 3-p Student t [L], Truncated Exponential [L], Wakeby [L], and
Weibull [L]. Multivariate sample L-comoments (LCMs) are implemented to
measure asymmetric associations.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ACKNOWLEDGEMENTS
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/ERRATA_FOR_ISBN9781463508418.txt
%doc %{rlibdir}/%{packname}/READMEinst
%{rlibdir}/%{packname}/testdata
%doc %{rlibdir}/%{packname}/WARRANTY
%{rlibdir}/%{packname}/INDEX
