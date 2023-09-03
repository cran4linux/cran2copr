%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  greport
%global packver   0.7-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.4
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical Reporting for Clinical Trials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rms >= 5.0.0
BuildRequires:    R-CRAN-Hmisc >= 4.0.0
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-rms >= 5.0.0
Requires:         R-CRAN-Hmisc >= 4.0.0
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-survival 
Requires:         R-methods 
Requires:         R-CRAN-data.table 

%description
Contains many functions useful for monitoring and reporting the results of
clinical trials and other experiments in which treatments are compared.
LaTeX is used to typeset the resulting reports, recommended to be in the
context of 'knitr'. The 'Hmisc', 'ggplot2', and 'lattice' packages are
used by 'greport' for high-level graphics.

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
