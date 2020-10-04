%global packname  phylolm
%global packver   2.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.2
Release:          2%{?dist}%{?buildtag}
Summary:          Phylogenetic Linear Regression

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-future.apply 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-future.apply 

%description
Provides functions for fitting phylogenetic linear models and phylogenetic
generalized linear models. The computation uses an algorithm that is
linear in the number of tips in the tree. The package also provides
functions for simulating continuous or binary traits along the tree. Other
tools include functions to test the adequacy of a population tree.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
