%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  priorCON
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Graph Community Detection Methods into Systematic Conservation Planning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-prioritizr >= 8.0.4
BuildRequires:    R-CRAN-tmap >= 3.3.4
BuildRequires:    R-CRAN-brainGraph >= 3.1.0
BuildRequires:    R-CRAN-igraph >= 2.0.3
BuildRequires:    R-CRAN-terra >= 1.7.78
BuildRequires:    R-CRAN-sf >= 1.0.16
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-highs 
Requires:         R-CRAN-prioritizr >= 8.0.4
Requires:         R-CRAN-tmap >= 3.3.4
Requires:         R-CRAN-brainGraph >= 3.1.0
Requires:         R-CRAN-igraph >= 2.0.3
Requires:         R-CRAN-terra >= 1.7.78
Requires:         R-CRAN-sf >= 1.0.16
Requires:         R-utils 
Requires:         R-CRAN-highs 

%description
An innovative tool-set that incorporates graph community detection methods
into systematic conservation planning. It is designed to enhance spatial
prioritization by focusing on the protection of areas with high ecological
connectivity. Unlike traditional approaches that prioritize individual
planning units, 'priorCON' focuses on clusters of features that exhibit
strong ecological linkages. The 'priorCON' package is built upon the
'prioritizr' package <doi:10.32614/CRAN.package.prioritizr>, using
commercial and open-source exact algorithm solvers that ensure optimal
solutions to prioritization problems.

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
