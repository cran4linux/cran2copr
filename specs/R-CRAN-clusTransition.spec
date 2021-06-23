%global __brp_check_rpaths %{nil}
%global packname  clusTransition
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Monitor Changes in Cluster Solutions of Dynamic Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-flexclust 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
Requires:         R-CRAN-flexclust 
Requires:         R-methods 
Requires:         R-graphics 

%description
Monitor and trace changes in clustering solutions of accumulating datasets
at successive time points. The clusters can adopt External and Internal
transition at succeeding time points. The External transitions comprise of
Survived, Merged, Split, Disappeared, and newly Emerged candidates. In
contrast, Internal transition includes changes in location and cohesion of
the survived clusters. The package uses MONIC framework developed by
Spiliopoulou, Ntoutsi, Theodoridis, and Schult
(2006)<doi:10.1145/1150402.1150491> .

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
