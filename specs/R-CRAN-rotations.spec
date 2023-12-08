%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rotations
%global packver   1.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.5
Release:          1%{?dist}%{?buildtag}
Summary:          Working with Rotation Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-Rcpp 

%description
Tools for working with rotational data, including simulation from the most
commonly used distributions on SO(3), methods for different Bayes, mean
and median type estimators for the central orientation of a sample,
confidence/credible regions for the central orientation based on those
estimators and a novel visualization technique for rotation data.  Most
recently, functions to identify potentially discordant (outlying) values
have been added.  References: Bingham, Melissa A. and Nordman, Dan J. and
Vardeman, Steve B. (2009), Bingham, Melissa A and Vardeman, Stephen B and
Nordman, Daniel J (2009), Bingham, Melissa A and Nordman, Daniel J and
Vardeman, Stephen B (2010), Leon, C.A. and Masse, J.C. and Rivest, L.P.
(2006), Hartley, R and Aftab, K and Trumpf, J. (2011), Stanfill, Bryan and
Genschel, Ulrike and Hofmann, Heike (2013), Maonton, Jonathan (2004),
Mardia, KV and Jupp, PE (2000, ISBN:9780471953333), Rancourt, D. and
Rivest, L.P. and Asselin, J. (2000), Chang, Ted and Rivest, Louis-Paul
(2001), Fisher, Nicholas I. (1996, ISBN:0521568900).

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
