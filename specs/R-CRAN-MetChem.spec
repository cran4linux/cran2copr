%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MetChem
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Chemical Structural Similarity Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rcdk >= 3.4.3
BuildRequires:    R-CRAN-KODAMA >= 2.3
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-fingerprint 
Requires:         R-CRAN-rcdk >= 3.4.3
Requires:         R-CRAN-KODAMA >= 2.3
Requires:         R-stats 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-fingerprint 

%description
A new pipeline to explore chemical structural similarity across
metabolite. It allows to classify metabolites in structurally-related
modules and identify common shared functional groups. KODAMA algorithm is
used to highlight structural similarity between metabolites. See
Cacciatore S, Tenori L, Luchinat C, Bennett PR, MacIntyre DA. (2017)
Bioinformatics <doi:10.1093/bioinformatics/btw705> and Cacciatore S,
Luchinat C, Tenori L. (2014) Proc Natl Acad Sci USA
<doi:10.1073/pnas.1220873111>.

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
