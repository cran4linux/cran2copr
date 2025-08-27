%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dataset
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Data Frames for Exchange and Reuse

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-ISOcodes 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-ISOcodes 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 

%description
The 'dataset' package helps create semantically rich, machine-readable,
and interoperable datasets in R. It extends tidy data frames with metadata
that preserves meaning, improves interoperability, and makes datasets
easier to publish, exchange, and reuse in line with ISO and W3C standards.

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
