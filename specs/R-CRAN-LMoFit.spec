%global packname  LMoFit
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced L-Moment Fitting of Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-lmom 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-utils 
Requires:         R-CRAN-lmom 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sf 
Requires:         R-utils 

%description
A complete framework for frequency analysis is provided by 'LMoFit'. It
has functions related to the determination of sample L-moments as in
Hosking, J.R.M. (1990) <doi:10.1111/j.2517-6161.1990.tb01775.x>, the
fitting of various distributions as in Zaghloul et al. (2020)
<doi:10.1016/j.advwatres.2020.103720> and Hosking, J.R.M. (2019)
<https://CRAN.R-project.org/package=lmom>, besides plotting and
manipulating L-space diagrams as in Papalexiou, S.M. & Koutsoyiannis, D.
(2016) <doi:10.1016/j.advwatres.2016.05.005> for two-shape parametric
distributions on the L-moment ratio diagram. Additionally, the quantile,
probability density, and cumulative probability functions of various
distributions are provided in a user-friendly manner.

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
