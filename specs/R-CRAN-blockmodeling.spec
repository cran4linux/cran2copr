%global packname  blockmodeling
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Generalized and Classical Blockmodeling of Valued Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-parallel 

%description
This is primarily meant as an implementation of generalized blockmodeling
for valued networks. In addition, measures of similarity or dissimilarity
based on structural equivalence and regular equivalence (REGE algorithms)
can be computed and partitioned matrices can be plotted: Žiberna
(2007)<doi:10.1016/j.socnet.2006.04.002>, Žiberna
(2008)<doi:10.1080/00222500701790207>, Žiberna
(2014)<doi:10.1016/j.socnet.2014.04.002>.

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
