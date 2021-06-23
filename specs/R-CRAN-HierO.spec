%global __brp_check_rpaths %{nil}
%global packname  HierO
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          A graphical user interface for calculating power and sample size for hierarchical data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    bwidget
Requires:         bwidget
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rneos 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tcltk2 
Requires:         R-methods 
Requires:         R-CRAN-rneos 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-XML 
Requires:         R-tcltk 
Requires:         R-CRAN-tcltk2 

%description
HierO is a graphical user interface (GUI) tool for calculating optimal
statistical power and sample size for hierarchical data structure. HierO
constructs a user defined sample size optimization problem to GAMS
(General Algebraic Modeling System)form and uses Rneos package to send the
problem to NEOS server for solving.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
