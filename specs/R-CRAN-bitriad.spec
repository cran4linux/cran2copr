%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bitriad
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Triadic Analysis of Affiliation Networks

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-igraph >= 1.1.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-igraph >= 1.1.2
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-MASS 

%description
Two principal tools are provided for the triadic analysis of affiliation
networks: triad census and triadic closure. These include several
variations on both classical tools tailored to affiliation network
structure; see Opsahl (2013) <doi:10.1016/j.socnet.2011.07.001>, Liebig
and Rao (2014) <doi:10.1109/SITIS.2014.15>, and Brunson (2015)
<doi:10.1017/nws.2015.38>. Additional functions support manipulation of
affiliation networks. Built on 'igraph' with new C++ calculations exposed
via 'Rcpp'.

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
