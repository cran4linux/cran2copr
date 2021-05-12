%global packname  InSilicoVA
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Probabilistic Verbal Autopsy Coding with 'InSilicoVA' Algorithm

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-InterVA5 
BuildRequires:    R-methods 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-InterVA5 
Requires:         R-methods 

%description
Computes individual causes of death and population cause-specific
mortality fractions using the 'InSilicoVA' algorithm from McCormick et al.
(2016) <DOI:10.1080/01621459.2016.1152191>. It uses data derived from
verbal autopsy (VA) interviews, in a format similar to the input of the
widely used 'InterVA4' method. This package provides general model fitting
and customization for 'InSilicoVA' algorithm and basic graphical
visualization of the output.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
