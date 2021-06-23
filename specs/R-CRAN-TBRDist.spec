%global __brp_check_rpaths %{nil}
%global packname  TBRDist
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Rearrangement Distances Between Unrooted Phylogenetic Trees

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-TreeTools >= 1.1.0
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-TreeDist 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-TreeTools >= 1.1.0
Requires:         R-CRAN-ape 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-TreeDist 

%description
Fast calculation of the Subtree Prune and Regraft (SPR), Tree Bisection
and Reconnection (TBR) and Replug distances between unrooted trees, using
the algorithms of Whidden and Matsen (2017) <arxiv:1511.07529>.

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
