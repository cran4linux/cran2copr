%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MleCensoR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Maximum Likelihood Estimation under Censoring Schemes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Provides generalized functions to compute Maximum Likelihood Estimation
(MLE) for any univariate distribution under various censoring and
truncation schemes.  Users supply the probability density function (PDF),
cumulative distribution function (CDF), survival function, support bounds,
and initial parameter values; the package constructs and maximizes the
appropriate log-likelihood automatically.  Supported schemes include right
and left truncation, random, right, left, interval, and middle censoring,
block random censoring, balanced joint progressive Type-II (BJPT-II),
progressive first failure, joint Type-I, Type-I, Type-II, progressive
Type-II, Type-II progressively hybrid, joint Type-II, hybrid, hybrid
Type-I, doubly Type-II, Type-I hybrid, and hybrid Type-II censoring.
Optimization methods include Newton-Raphson (NR),
Broyden-Fletcher-Goldfarb-Shanno (BFGS), the BFGS algorithm implemented in
R (BFGSR), Berndt-Hall-Hall-Hausman (BHHH), Simulated Annealing (SANN),
Conjugate Gradients (CG), and Nelder-Mead (NM).  Inference summaries
provide the Akaike Information Criterion (AIC), estimated coefficients,
log-likelihood, iteration count, standard errors, z-values, p-values, and
the variance-covariance matrix.  Methods are described in Nagar, Kumar,
and Krishna (2026) <doi:10.59467/IJASS.2026.22.1>, Goel, Kumar, and
Krishna (2026, "Estimation in power Lindley distributions using balanced
joint progressively Type-II censored data"), Wu and Kus (2009)
<doi:10.1016/j.csda.2009.03.010>, Goel and Krishna (2026)
<doi:10.1007/s13198-026-03208-w>, Balakrishnan and Aggarwala (2000,
ISBN:978-1-4612-1334-5), Mondal and Kundu (2020)
<doi:10.1080/03610926.2018.1554128>, Ding and Gui (2023)
<doi:10.3390/math11092003>, Prajapati, Mitra, and Kundu (2019)
<doi:10.1007/s13571-018-0167-0>, Yadav, Jaiswal, and Yadav (2026)
<doi:10.1007/s11135-026-02647-8>, Iyer, Jammalamadaka, and Kundu (2008)
<doi:10.1016/j.jspi.2007.03.062>, Banerjee and Kundu (2008)
<doi:10.1109/TR.2008.916890>, Kundu and Joarder (2006)
<doi:10.1016/j.csda.2005.05.002>, Berndt, Hall, Hall, and Hausman (1974)
"Estimation and Inference in Nonlinear Structural Models"
<doi:10.3386/t0003>, Fletcher (1987, "Practical Methods of Optimization",
ISBN:978-0-471-91547-8), Nelder and Mead (1965)
<doi:10.1093/comjnl/7.4.308>, McKinnon (1999) "Convergence of the
Nelder-Mead simplex method to a non-stationary point"
<doi:10.1137/S1052623496303482>, Kirkpatrick, Gelatt, and Vecchi (1983)
<doi:10.1126/science.220.4598.671>, Fletcher and Reeves (1964)
<doi:10.1093/comjnl/7.2.149>, and Nocedal and Wright (2006, "Numerical
Optimization", ISBN:978-0-387-30303-1).

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
