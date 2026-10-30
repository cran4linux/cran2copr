%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Entropic.Scree
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Information-Theoretic Measurement Mapping and Rank Estimation

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-infotheo 
Requires:         R-parallel 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-Rcpp 

%description
Maps relationships among measurements using a double-centered,
joint-entropy-normalized mutual information matrix. Provides
informational-axis loadings, primary and extended spectral-boundary
diagnostics, and spectral-volume and informational-gravity summaries for
discrete and discretized tabular data. The selected Primary Informational
Rank is a candidate information-spectrum boundary, not an identified
generating dimension. Optional, explicitly recorded missing-data
preparation supports categorical missing states and numeric median fills
with protected missingness indicators. For methodological details, see
Lee-St. John (2026) <doi:10.5281/zenodo.22028086>.

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
