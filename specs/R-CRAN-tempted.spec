%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tempted
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Temporal Tensor Decomposition, a Dimensionality Reduction Tool for Longitudinal Multivariate Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-methods >= 4.2.1
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-np >= 0.60.17
Requires:         R-methods >= 4.2.1
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-np >= 0.60.17

%description
TEMPoral TEnsor Decomposition (TEMPTED), is a dimension reduction method
for multivariate longitudinal data with varying temporal sampling. It
formats the data into a temporal tensor and decomposes it into a summation
of low-dimensional components, each consisting of a subject loading
vector, a feature loading vector, and a continuous temporal loading
function. These loadings provide a low-dimensional representation of
subjects or samples and can be used to identify features associated with
clusters of subjects or samples. TEMPTED provides the flexibility of
allowing subjects to have different temporal sampling, so time points do
not need to be binned, and missing time points do not need to be imputed.

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
