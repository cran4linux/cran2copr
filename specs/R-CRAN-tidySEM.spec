%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidySEM
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Structural Equation Modeling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-OpenMx 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-blavaan 
BuildRequires:    R-CRAN-MplusAutomation 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-bain 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-progressr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-OpenMx 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-blavaan 
Requires:         R-CRAN-MplusAutomation 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-psych 
Requires:         R-methods 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-bain 
Requires:         R-CRAN-car 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-progressr 

%description
A tidy workflow for generating, estimating, reporting, and plotting
structural equation models using 'lavaan', 'OpenMx', or 'Mplus'.
Throughout this workflow, elements of syntax, results, and graphs are
represented as 'tidy' data, making them easy to customize.

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
