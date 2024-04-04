%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fase
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Adjacency Spectral Embedding

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rTensor >= 1.4.8
BuildRequires:    R-CRAN-splines2 >= 0.4.7
BuildRequires:    R-CRAN-RSpectra >= 0.16.1
Requires:         R-CRAN-rTensor >= 1.4.8
Requires:         R-CRAN-splines2 >= 0.4.7
Requires:         R-CRAN-RSpectra >= 0.16.1

%description
Latent process embedding for functional network data with the Functional
Adjacency Spectral Embedding. Fits smooth latent processes based on cubic
spline bases. Also generates functional network data from three models,
and evaluates a network generalized cross-validation criterion for
dimension selection. For more information, see MacDonald, Zhu and Levina
(2022+) <arXiv:2210.07491>.

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
