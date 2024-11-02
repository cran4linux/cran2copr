%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  slca
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Structural Modeling for Multiple Latent Class Variables

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Provides comprehensive tools for the implementation of Structural Latent
Class Models (SLCM), including Latent Transition Analysis (LTA; Linda M.
Collins and Stephanie T. Lanza, 2009) <doi:10.1002/9780470567333>, Latent
Class Profile Analysis (LCPA; Hwan Chung et al., 2010)
<doi:10.1111/j.1467-985x.2010.00674.x>, and Joint Latent Class Analysis
(JLCA; Saebom Jeon et al., 2017) <doi:10.1080/10705511.2017.1340844>, and
any other extended models involving multiple latent class variables.

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
