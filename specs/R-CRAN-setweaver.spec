%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  setweaver
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Building Sets of Variables in a Probabilistic Framework

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-permutes >= 2.8
BuildRequires:    R-CRAN-igraph >= 2.1.2
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-pheatmap >= 1.0.13
BuildRequires:    R-CRAN-splitTools >= 1.0.1
Requires:         R-CRAN-permutes >= 2.8
Requires:         R-CRAN-igraph >= 2.1.2
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-pheatmap >= 1.0.13
Requires:         R-CRAN-splitTools >= 1.0.1

%description
Create sets of variables based on a mutual information approach. In this
context, a set is a collection of distinct elements (e.g., variables) that
can also be treated as a single entity.  Mutual information, a concept
from probability theory, quantifies the dependence between two variables
by expressing how much information about one variable can be gained from
observing the other. Furthermore, you can analyze, and visualize these
sets in order to better understand the relationships among variables.

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
