%global __brp_check_rpaths %{nil}
%global packname  simplextree
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Provides Tools for Working with General Simplicial Complexes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-methods 
Requires:         R-CRAN-magrittr 

%description
Provides an interface to a Simplex Tree data structure, which is a data
structure aimed at enabling efficient manipulation of simplicial complexes
of any dimension. The Simplex Tree data structure was originally
introduced by Jean-Daniel Boissonnat and Clément Maria (2014)
<doi:10.1007/s00453-014-9887-3>.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
