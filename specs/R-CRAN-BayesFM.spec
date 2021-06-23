%global __brp_check_rpaths %{nil}
%global packname  BayesFM
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Inference for Factor Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-checkmate >= 1.8.0
BuildRequires:    R-CRAN-plyr >= 1.8.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-checkmate >= 1.8.0
Requires:         R-CRAN-plyr >= 1.8.0
Requires:         R-CRAN-coda 
Requires:         R-CRAN-gridExtra 

%description
Collection of procedures to perform Bayesian analysis on a variety of
factor models. Currently, it includes: Bayesian Exploratory Factor
Analysis (befa), an approach to dedicated factor analysis with stochastic
search on the structure of the factor loading matrix. The number of latent
factors, as well as the allocation of the manifest variables to the
factors, are not fixed a priori but determined during MCMC sampling. More
approaches will be included in future releases of this package.

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
