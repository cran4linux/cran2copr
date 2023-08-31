%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NMA
%global packver   1.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Network Meta-Analysis Based on Multivariate Meta-Analysis Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-forestplot 
Requires:         R-stats 
Requires:         R-grid 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-forestplot 

%description
Network meta-analysis tools based on contrast-based approach using the
multivariate meta-analysis and meta-regression models (Noma et al. (2023)
<Forthcoming>). Standard analysis tools for network meta-analysis and
meta-regression (e.g., synthesis analysis, ranking analysis, and creating
league table) are available by simple commands. For inconsistency
analyses, the local and global inconsistency tests based on the Higgins'
design-by-treatment interaction model can be applied. Also, the
side-splitting and the Jackson's random inconsistency model are available.
Standard graphical tools for network meta-analysis (e.g., network plot,
ranked forest plot, and transitivity analysis) can also be utilized. For
the synthesis analyses, the Noma-Hamura's improved REML (restricted
maximum likelihood)-based methods (Noma et al. (2023)
<doi:10.1002/jrsm.1652> <doi:10.1002/jrsm.1651>) are adopted as the
default methods.

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
