%global __brp_check_rpaths %{nil}
%global packname  CEOdata
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Datasets of the CEO (Centre d'Estudis d'Opinio) for Opinion Polls in Catalonia

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-haven 
Requires:         R-CRAN-urltools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-jsonlite 

%description
Easy and convenient access to the datasets / microdata of the "Centre
d'Estudis d'Opinió", the Catalan institution for polling and public
opinion.  The package uses the data stored in the servers of the CEO and
returns it in a tidy format (tibble).

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
