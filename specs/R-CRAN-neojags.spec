%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  neojags
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Neo-Normal Distributions Family for Markov Chain Monte Carlo (MCMC) Models in 'JAGS'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-runjags 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-runjags 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-coda 

%description
A 'JAGS' extension module provides neo-normal distributions family
including MSNBurr, MSNBurr-IIa, GMSNBurr, Lunetta Exponential Power,
Fernandez-Steel Skew t, Fernandez-Steel Skew Normal,
Fernandez-Osiewalski-Steel Skew Exponential Power, Jones Skew Exponential
Power. References: Choir, A. S. (2020). "The New Neo-Normal Distributions
and Their Properties".Unpublished Dissertation. Denwood, M.J. (2016)
<doi:10.18637/jss.v071.i09>. Fernandez, C., Osiewalski, J., & Steel, M. F.
(1995) <doi:10.1080/01621459.1995.10476637>. Fernandez, C., & Steel, M. F.
(1998) <doi:10.1080/01621459.1998.10474117>. Iriawan, N. (2000).
"Computationally Intensive Approaches to Inference in NeoNormal Linear
Models".Unpublished Dissertation. Mineo, A., & Ruggieri, M. (2005)
<doi:10.18637/jss.v012.i04>. Rigby, R. A., & Stasinopoulos, D. M. (2005)
<doi:10.1111/j.1467-9876.2005.00510.x>. Lunetta, G. (1963). "Di una
Generalizzazione dello Schema della Curva Normale". Rigby, R. A.,
Stasinopoulos, M. D., Heller, G. Z., & Bastiani, F. D. (2019)
<doi:10.1201/9780429298547>.

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
