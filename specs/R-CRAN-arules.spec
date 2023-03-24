%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  arules
%global packver   1.7-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.6
Release:          1%{?dist}%{?buildtag}
Summary:          Mining Association Rules and Frequent Itemsets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Matrix >= 1.4.0
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-Matrix >= 1.4.0
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-generics 
Requires:         R-graphics 
Requires:         R-utils 

%description
Provides the infrastructure for representing, manipulating and analyzing
transaction data and patterns (frequent itemsets and association rules).
Also provides C implementations of the association mining algorithms
Apriori and Eclat. Hahsler, Gruen and Hornik (2005)
<doi:10.18637/jss.v014.i15>.

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
