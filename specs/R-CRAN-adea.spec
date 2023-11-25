%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adea
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Alternate DEA Package

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-ROI.plugin.glpk 
BuildRequires:    R-CRAN-ROI.plugin.lpsolve 
BuildRequires:    R-CRAN-ROI.plugin.symphony 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lpSolveAPI 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-ROI 
BuildRequires:    R-CRAN-slam 
Requires:         R-methods 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-ROI.plugin.glpk 
Requires:         R-CRAN-ROI.plugin.lpsolve 
Requires:         R-CRAN-ROI.plugin.symphony 
Requires:         R-CRAN-combinat 
Requires:         R-graphics 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lpSolveAPI 
Requires:         R-parallel 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-ROI 
Requires:         R-CRAN-slam 

%description
The meaning of adea is "alternate DEA". This package is devoted to provide
the alternative method of DEA described in the paper entitled "Stepwise
Selection of Variables in DEA Using Contribution Load", by F.
Fernandez-Palacin, M. A. Lopez-Sanchez and M. Munoz-Marquez. Pesquisa
Operacional 38 (1), pg. 1-24, 2018.
<doi:10.1590/0101-7438.2018.038.01.0031>. A full functional on-line and
interactive version is available at <https://knuth.uca.es/shiny/DEA/>.

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
