%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ganGenerativeData
%global packver   1.5.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.6
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Generative Data for a Data Source

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-tensorflow >= 2.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-tensorflow >= 2.0.0
Requires:         R-CRAN-Rcpp >= 1.0.3

%description
Generative Adversarial Networks are applied to generate generative data
for a data source. A generative model consisting of a generator and a
discriminator network is trained. In iterated training steps the
distribution of generated data is converging to that of the data source.
Direct applications of generative data are the created functions for data
classifying and missing data completion. Reference: Goodfellow et al.
(2014) <arXiv:1406.2661v1>.

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
