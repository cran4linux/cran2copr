%global __brp_check_rpaths %{nil}
%global packname  Rchoice
%global packver   0.3-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Discrete Choice (Binary, Poisson and Ordered) Models with Random Parameters

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-miscTools 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-memisc 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-miscTools 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-memisc 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-plotrix 
Requires:         R-stats 
Requires:         R-graphics 

%description
An implementation of simulated maximum likelihood method for the
estimation of Binary (Probit and Logit), Ordered (Probit and Logit) and
Poisson models with random parameters for cross-sectional and longitudinal
data as presented in Sarrias (2016) <doi:10.18637/jss.v074.i10>.

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
