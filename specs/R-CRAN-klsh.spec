%global __brp_check_rpaths %{nil}
%global packname  klsh
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Blocking for Record Linkage

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-blink 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-SnowballC 
Requires:         R-CRAN-blink 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-SnowballC 

%description
An implementation of the blocking algorithm KLSH in Steorts, Ventura,
Sadinle, Fienberg (2014) <DOI:10.1007/978-3-319-11257-2_20>, which is a
k-means variant of locality sensitive hashing. The method is illustrated
with examples and a vignette.

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
