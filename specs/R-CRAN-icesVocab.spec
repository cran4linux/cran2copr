%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  icesVocab
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          ICES Vocabularies Database Web Services

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-icesConnect >= 1.1.4
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-cachem 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-icesConnect >= 1.1.4
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-cachem 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-httr 

%description
R interface to access the Vocabularies REST API of the ICES (International
Council for the Exploration of the Sea) Vocabularies database
<https://vocab.ices.dk/services/>.

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
