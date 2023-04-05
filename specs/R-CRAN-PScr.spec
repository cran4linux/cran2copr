%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PScr
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation for the Power Series Cure Rate Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-VGAM 

%description
Provide estimation for particular cases of the power series cure rate
model <doi:10.1080/03610918.2011.639971>. For the distribution of the
concurrent causes the alternative models are the Poisson, logarithmic,
negative binomial and Bernoulli (which are includes in the original work),
the polylogarithm model <doi:10.1080/00949655.2018.1451850> and the
Flory-Schulz <doi:10.3390/math10244643>. The estimation procedure is based
on the EM algorithm discussed in <doi:10.1080/03610918.2016.1202276>. For
the distribution of the time-to-event the alternative models are slash
half-normal, Weibull, gamma and Birnbaum-Saunders distributions.

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
