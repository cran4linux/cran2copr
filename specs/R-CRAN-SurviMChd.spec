%global packname  SurviMChd
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          High Dimensional Survival Data Analysis with Markov Chain Monte Carlo

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-icenReg 
BuildRequires:    R-CRAN-ICBayes 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-survival 
Requires:         R-utils 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-icenReg 
Requires:         R-CRAN-ICBayes 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 

%description
High dimensional survival data analysis with Markov Chain Monte
Carlo(MCMC). Currently support frailty data analysis. Allows for Weibull
and Exponential distribution. Includes function for interval censored
data.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
