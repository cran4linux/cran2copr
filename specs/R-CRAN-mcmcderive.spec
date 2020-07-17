%global packname  mcmcderive
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Derive MCMC Parameters

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-mcmcr >= 0.3.0
BuildRequires:    R-CRAN-chk 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-universals 
BuildRequires:    R-CRAN-extras 
BuildRequires:    R-CRAN-term 
BuildRequires:    R-CRAN-nlist 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-mcmcr >= 0.3.0
Requires:         R-CRAN-chk 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-universals 
Requires:         R-CRAN-extras 
Requires:         R-CRAN-term 
Requires:         R-CRAN-nlist 
Requires:         R-CRAN-purrr 

%description
Generates derived parameter(s) from Monte Carlo Markov Chain (MCMC)
samples using R code. This allows Bayesian models to be fitted without the
inclusion of derived parameters which add unnecessary clutter and slow
model fitting. For more information on MCMC samples see Brooks et al.
(2011) <isbn:978-1-4200-7941-8>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
