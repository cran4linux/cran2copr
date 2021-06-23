%global __brp_check_rpaths %{nil}
%global packname  SDEFSR
%global packver   0.7.22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.22
Release:          1%{?dist}%{?buildtag}
Summary:          Subgroup Discovery with Evolutionary Fuzzy Systems

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 0.11
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-shiny >= 0.11
Requires:         R-CRAN-foreign 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 

%description
Implementation of evolutionary fuzzy systems for the data mining task
called "subgroup discovery". In particular, the algorithms presented in
this package are: M. J. del Jesus, P. Gonzalez, F. Herrera, M. Mesonero
(2007) <doi:10.1109/TFUZZ.2006.890662> M. J. del Jesus, P. Gonzalez, F.
Herrera (2007) <doi:10.1109/MCDM.2007.369416> C. J. Carmona, P. Gonzalez,
M. J. del Jesus, F. Herrera (2010) <doi:10.1109/TFUZZ.2010.2060200> C. J.
Carmona, V. Ruiz-Rodado, M. J. del Jesus, A. Weber, M. Grootveld, P.
González, D. Elizondo (2015) <doi:10.1016/j.ins.2014.11.030> It also
provide a Shiny App to ease the analysis. The algorithms work with data
sets provided in KEEL, ARFF and CSV format and also with data.frame
objects.

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
