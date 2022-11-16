%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simplifyNet
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Network Sparsification

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-methods >= 4.0.2
BuildRequires:    R-stats >= 4.0.2
BuildRequires:    R-CRAN-igraph >= 1.3.1
BuildRequires:    R-CRAN-Matrix >= 1.2.18
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-sanic >= 0.0.1
Requires:         R-methods >= 4.0.2
Requires:         R-stats >= 4.0.2
Requires:         R-CRAN-igraph >= 1.3.1
Requires:         R-CRAN-Matrix >= 1.2.18
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-sanic >= 0.0.1

%description
Network sparsification with a variety of novel and known network
sparsification techniques. All network sparsification techniques reduce
the number of edges, not the number of nodes. Network sparsification is
sometimes referred to as network dimensionality reduction. This package is
based on the work of Spielman, D., Srivastava, N. (2009)<arXiv:0803.0929>.
Koutis I., Levin, A., Peng, R. (2013)<arXiv:1209.5821>. Toivonen, H.,
Mahler, S., Zhou, F. (2010)<doi:10.1007>. Foti, N., Hughes, J., Rockmore,
D. (2011)<doi:10.1371>.

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
