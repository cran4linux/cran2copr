%global packname  surface
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Hansen Models to Investigate Convergent Evolution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6
Requires:         R-core >= 2.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-ouch 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-methods 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-ouch 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-geiger 
Requires:         R-methods 

%description
This data-driven phylogenetic comparative method fits stabilizing
selection models to continuous trait data, building on the 'ouch'
methodology of Butler and King (2004) <doi:10.1086/426002>. The main
functions fit a series of Hansen models using stepwise AIC, then identify
cases of convergent evolution where multiple lineages have shifted to the
same adaptive peak. For more information see Ingram and Mahler (2013)
<doi:10.1111/2041-210X.12034>.

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
