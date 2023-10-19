%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpatEntropy
%global packver   2.2-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Entropy Measures

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat >= 3.0.2
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-spatstat >= 3.0.2
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.random 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
The heterogeneity of spatial data presenting a finite number of categories
can be measured via computation of spatial entropy. Functions are
available for the computation of the main entropy and spatial entropy
measures in the literature. They include the traditional version of
Shannon's entropy (Shannon, 1948
<doi:10.1002/j.1538-7305.1948.tb01338.x>), Batty's spatial entropy (Batty,
1974 <doi:10.1111/j.1538-4632.1974.tb01014.x>), O'Neill's entropy (O'Neill
et al., 1998 <doi:10.1007/BF00162741>), Li and Reynolds' contagion index
(Li and Reynolds, 1993 <doi:10.1007/BF00125347>), Karlstrom and Ceccato's
entropy (Karlstrom and Ceccato, 2002
<https://urn.kb.se/resolve?urn=urn:nbn:se:kth:diva-61351>), Leibovici's
entropy (Leibovici, 2009 <doi:10.1007/978-3-642-03832-7_24>), Parresol and
Edwards' entropy (Parresol and Edwards, 2014 <doi:10.3390/e16041842>) and
Altieri's entropy (Altieri et al., 2018, <doi:10.1007/s10651-017-0383-1>).
Full references for all measures can be found under the topic
'SpatEntropy'. The package is able to work with lattice and point data.
The updated version works with the updated 'spatstat' package (>= 3.0-2).

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
