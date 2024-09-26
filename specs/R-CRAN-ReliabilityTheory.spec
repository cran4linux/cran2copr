%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ReliabilityTheory
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Structural Reliability Analysis

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-PhaseType >= 0.2.0
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-FRACTION 
BuildRequires:    R-CRAN-mcmc 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-utils 
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-PhaseType >= 0.2.0
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-FRACTION 
Requires:         R-CRAN-mcmc 
Requires:         R-CRAN-sfsmisc 
Requires:         R-utils 

%description
Perform structural reliability analysis, including computation and
simulation with system signatures, Samaniego (2007)
<doi:10.1007/978-0-387-71797-5>, and survival signatures, Coolen and
Coolen-Maturi (2013) <doi:10.1007/978-3-642-30662-4_8>. Additionally
supports parametric and topological inference given system lifetime data,
Aslett (2012) <https://www.louisaslett.com/PhD_Thesis.pdf>.

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
