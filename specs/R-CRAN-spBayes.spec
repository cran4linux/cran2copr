%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spBayes
%global packver   0.4-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.8
Release:          1%{?dist}%{?buildtag}
Summary:          Univariate and Multivariate Spatial-Temporal Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-Matrix 

%description
Fits univariate and multivariate spatio-temporal random effects models for
point-referenced data using Markov chain Monte Carlo (MCMC). Details are
given in Finley, Banerjee, and Gelfand (2015) <doi:10.18637/jss.v063.i13>
and Finley and Banerjee <doi:10.1016/j.envsoft.2019.104608>.

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
