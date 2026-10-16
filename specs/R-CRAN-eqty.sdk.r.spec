%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eqty.sdk.r
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Verifiable Provenance for 'R' Workflows

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.41
Requires:         R-CRAN-reticulate >= 1.41

%description
Provides an 'R' interface for building verifiable manifests around data,
models, prompts, agents, computations, and related lineage. Exposes the
public 'eqty-sdk' 'Python' package through types accessible from 'R' for
creating assets, connecting computation inputs and outputs by content
identifier, grouping statements in contexts, and exporting manifest JSON
files.

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
