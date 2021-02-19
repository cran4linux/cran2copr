%global packname  DMTL
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Applying Distribution Mapping Based Transfer Learning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0.86
BuildRequires:    R-CRAN-randomForest >= 4.6.14
BuildRequires:    R-CRAN-glmnet >= 4.1
BuildRequires:    R-CRAN-ks >= 1.11.7
BuildRequires:    R-CRAN-kernlab >= 0.9.29
Requires:         R-CRAN-caret >= 6.0.86
Requires:         R-CRAN-randomForest >= 4.6.14
Requires:         R-CRAN-glmnet >= 4.1
Requires:         R-CRAN-ks >= 1.11.7
Requires:         R-CRAN-kernlab >= 0.9.29

%description
Implementation of a transfer learning framework employing distribution
mapping based domain transfer. Uses the renowned concept of histogram
matching (see Gonzalez and Fittes (1977)
<doi:10.1016/0094-114X(77)90062-3>, Gonzalez and Woods (2008)
<isbn:9780131687288>) and extends it to include distribution measures like
kernel density estimates (KDE; see Wand and Jones (1995)
<isbn:978-0-412-55270-0>, Jones et al. (1996) <doi:10.2307/2291420). In
the typical application scenario, one can use the underlying sample
distributions (histogram or KDE) to generate a map between two distinct
but related domains to transfer the target data to the source domain and
utilize the available source data for better predictive modeling design.
Suitable for the case where a one-to-one sample matching is not possible,
thus one needs to transform the underlying data distribution to utilize
the more available data for modeling.

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
