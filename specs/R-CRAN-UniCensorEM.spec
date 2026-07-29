%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  UniCensorEM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          EM Algorithm for Parameter Estimation Under Censoring Schemes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 

%description
Performs parameter estimation using the Expectation-Maximization (EM)
algorithm of Dempster, Laird, and Rubin (1977)
<doi:10.1111/j.2517-6161.1977.tb01600.x> for arbitrary univariate
probability distributions under numerous censoring and truncation schemes.
Users supply the probability density function (PDF), cumulative
distribution function (CDF), survival function, initial parameter vector,
support bounds, and observed data; the package automatically estimates
parameters using the EM algorithm under the specified censoring scheme.
Supported schemes include complete data, right censoring, left censoring,
interval censoring, random censoring, block random censoring, Type-I
censoring, Type-II censoring, progressive Type-II censoring (Balakrishnan
and Aggarwala (2000, ISBN:978-1-4612-1334-5)), progressive first failure
censoring, joint Type-I censoring, joint Type-II censoring, balanced joint
progressive Type-II censoring, hybrid censoring, hybrid Type-I censoring,
hybrid Type-II censoring, Type-I hybrid censoring, Type-II progressively
hybrid censoring, doubly Type-II censoring, middle censoring, right
truncation, and left truncation. Standard errors are computed via the
observed information matrix (numerical Hessian), the Louis (1982)
<doi:10.1111/j.2517-6161.1982.tb01203.x> method, and the supplemented EM
(SEM) algorithm of Meng and Rubin (1991)
<doi:10.1080/01621459.1991.10475130>. The package also provides confidence
intervals, model selection criteria (AIC, BIC, AICc, HQIC),
goodness-of-fit statistics (Kolmogorov-Smirnov, Cramer-von Mises,
Anderson-Darling), residual analysis (randomized quantile residuals,
generalized residuals), parametric bootstrap methods, Aitken acceleration
for convergence improvement, and comprehensive visualization tools.
References: Wu and Kus (2009) <doi:10.1016/j.csda.2009.03.010>, Kundu and
Joarder (2006) <doi:10.1016/j.csda.2005.05.002>, Iyer, Jammalamadaka, and
Kundu (2008) <doi:10.1016/j.jspi.2007.03.062>, Banerjee and Kundu (2008)
<doi:10.1109/TR.2008.916890>, Prajapati, Mitra, and Kundu (2019)
<doi:10.1007/s13571-018-0167-0>, Mondal and Kundu (2020)
<doi:10.1080/03610926.2018.1554128>, Ding and Gui (2023)
<doi:10.3390/math11092003>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
