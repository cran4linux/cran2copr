%global __brp_check_rpaths %{nil}
%global packname  rdryad
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}%{?buildtag}
Summary:          Access for Dryad Web Services

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-hoardr 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-mime 
Requires:         R-CRAN-crul 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-hoardr 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-mime 

%description
Interface to the Dryad "Solr" API, their "OAI-PMH" service, and fetch
datasets. Dryad (<https://datadryad.org/>) is a curated host of data
underlying scientific publications.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
