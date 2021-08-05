%global __brp_check_rpaths %{nil}
%global packname  degross
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Density Estimation from GROuped Summary Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cubicBsplines 
BuildRequires:    R-stats 
Requires:         R-CRAN-cubicBsplines 
Requires:         R-stats 

%description
Estimation of a density from grouped (tabulated) summary statistics
evaluated in each of the big bins (or classes) partitioning the support of
the variable. These statistics include class frequencies and central
moments of order one up to four. The log-density is modelled using a
linear combination of penalised B-splines. The multinomial log-likelihood
involving the frequencies adds up to a roughness penalty based on the
differences in the coefficients of neighbouring B-splines and the log of a
root-n approximation of the sampling density of the observed vector of
central moments in each class. The so-obtained penalized log-likelihood is
maximized using the EM algorithm to get an estimate of the spline
parameters and, consequently, of the variable density and related
quantities such as quantiles, see Lambert, P. (2021) <arXiv:2107.03883>
for details.

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
