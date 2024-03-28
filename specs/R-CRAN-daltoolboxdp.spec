%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  daltoolboxdp
%global packver   1.0.767
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.767
Release:          1%{?dist}%{?buildtag}
Summary:          Data Pre-Processing Extensions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-daltoolbox 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-FSelector 
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-smotefamily 
Requires:         R-CRAN-daltoolbox 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-FSelector 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-smotefamily 

%description
An important aspect of data analytics is related to data management
support for artificial intelligence. It is related to preparing data
correctly. This package provides extensions to support data preparation in
terms of both data sampling and data engineering. Overall, the package
provides researchers with a comprehensive set of functionalities for data
science based on experiment lines, promoting ease of use, extensibility,
and integration with various tools and libraries. Information on
Experiment Line is based on Ogasawara et al. (2009)
<doi:10.1007/978-3-642-02279-1_20>.

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
