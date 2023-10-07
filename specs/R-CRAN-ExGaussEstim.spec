%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ExGaussEstim
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Quantile Maximization Likelihood Estimation and Bayesian Ex-Gaussian Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-invgamma 
BuildRequires:    R-CRAN-dlm 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-gamlss.dist 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-invgamma 
Requires:         R-CRAN-dlm 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-gamlss.dist 

%description
Presents two methods to estimate the parameters 'mu', 'sigma', and 'tau'
of an ex-Gaussian distribution. Those methods are Quantile Maximization
Likelihood Estimation ('QMLE') and Bayesian. The 'QMLE' method allows a
choice between three different estimation algorithms for these parameters
: 'neldermead' ('NEMD'), 'fminsearch' ('FMIN'), and 'nlminb' ('NLMI'). For
more details about the methods you can refer at the following list: Brown,
S., & Heathcote, A. (2003) <doi:10.3758/BF03195527>; McCormack, P. D., &
Wright, N. M. (1964) <doi:10.1037/h0083285>; Van Zandt, T. (2000)
<doi:10.3758/BF03214357>; El Haj, A., Slaoui, Y., Solier, C., & Perret, C.
(2021) <doi:10.19139/soic-2310-5070-1251>; Gilks, W. R., Best, N. G., &
Tan, K. K. C. (1995) <doi:10.2307/2986138>.

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
