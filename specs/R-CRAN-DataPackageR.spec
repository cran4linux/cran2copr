%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DataPackageR
%global packver   0.16.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.1
Release:          1%{?dist}%{?buildtag}
Summary:          Construct Reproducible Analytic Data Sets as R Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-pkgbuild 
BuildRequires:    R-CRAN-pkgload 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-pkgbuild 
Requires:         R-CRAN-pkgload 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-roxygen2 
Requires:         R-CRAN-rprojroot 
Requires:         R-CRAN-usethis 
Requires:         R-utils 
Requires:         R-CRAN-yaml 

%description
A framework to help construct R data packages in a reproducible manner.
Potentially time consuming processing of raw data sets into analysis ready
data sets is done in a reproducible manner and decoupled from the usual 'R
CMD build' process so that data sets can be processed into R objects in
the data package and the data package can then be shared, built, and
installed by others without the need to repeat computationally costly data
processing.  The package maintains data provenance by turning the data
processing scripts into package vignettes, as well as enforcing
documentation and version checking of included data objects. Data packages
can be version controlled on 'GitHub', and used to share data for
manuscripts, collaboration and reproducible research.

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
