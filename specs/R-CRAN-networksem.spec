%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  networksem
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Network Structural Equation Modeling

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-latentnet 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-influential 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
Requires:         R-CRAN-latentnet 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-influential 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-network 
Requires:         R-CRAN-igraph 
Requires:         R-methods 

%description
Several methods have been developed to integrate structural equation
modeling techniques with network data analysis to examine the relationship
between network and non-network data. Both node-based and edge-based
information can be extracted from the network data to be used as observed
variables in structural equation modeling. To facilitate the application
of these methods, model specification can be performed in the familiar
syntax of the 'lavaan' package, ensuring ease of use for researchers.
Technical details and examples can be found at
<https://bigsem.psychstat.org>.

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
