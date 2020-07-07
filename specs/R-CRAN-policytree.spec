%global packname  policytree
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Policy Learning via Doubly Robust Empirical Welfare Maximizationover Trees

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-grf >= 1.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-grf >= 1.1.0
Requires:         R-CRAN-Rcpp 

%description
Learn optimal policies via doubly robust empirical welfare maximization
over trees. This package implements the multi-action doubly robust
approach of Zhou, Athey and Wager (2018) <arXiv:1810.04778> in the case
where we want to learn policies that belong to the class of depth k
decision trees.

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
