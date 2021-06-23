%global __brp_check_rpaths %{nil}
%global packname  riskmetric
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Risk Metrics to Evaluating R Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-BiocManager 
BuildRequires:    R-CRAN-cranlogs 
BuildRequires:    R-CRAN-covr 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-devtools 
Requires:         R-CRAN-backports 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-urltools 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-BiocManager 
Requires:         R-CRAN-cranlogs 
Requires:         R-CRAN-covr 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-devtools 

%description
Facilities for assessing R packages against a number of metrics to help
quantify their robustness.

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
