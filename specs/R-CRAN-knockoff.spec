%global __brp_check_rpaths %{nil}
%global packname  knockoff
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          The Knockoff Filter for Controlled Variable Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rdsdp 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-Rdsdp 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-gtools 
Requires:         R-utils 

%description
The knockoff filter is a general procedure for controlling the false
discovery rate (FDR) when performing variable selection. For more
information, see the website below and the accompanying paper: Candes et
al., "Panning for gold: model-X knockoffs for high-dimensional controlled
variable selection", J. R. Statist. Soc. B (2018) 80, 3, pp. 551-577.

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
