%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TDIagree
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Assessment of Agreement using the Total Deviation Index

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plotfunctions 
BuildRequires:    R-CRAN-coxed 
BuildRequires:    R-CRAN-katex 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-nlme 
Requires:         R-stats 
Requires:         R-CRAN-plotfunctions 
Requires:         R-CRAN-coxed 
Requires:         R-CRAN-katex 

%description
The total deviation index (TDI) is an unscaled statistical measure used to
evaluate the deviation between paired quantitative measurements when
assessing the extent of agreement between different raters. It describes a
boundary such that a large specified proportion of the differences in
paired measurements are within the boundary (Lin, 2000)
<https://pubmed.ncbi.nlm.nih.gov/10641028/>. This R package implements
some methodologies existing in the literature for TDI estimation and
inference in the case of two raters.

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
