%global packname  treedata.table
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Manipulation of Matched Phylogenies and Data using 'data.table'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-geiger 
Requires:         R-utils 
Requires:         R-CRAN-data.table 

%description
An implementation that combines trait data and a phylogenetic tree (or
trees) into a single object of class treedata.table. The resulting object
can be easily manipulated to simultaneously change the trait- and
tree-level sampling. Currently implemented functions allow users to use a
'data.table' syntax when performing operations on the trait dataset within
the treedata.table object.

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
