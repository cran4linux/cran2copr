%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forrel
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Forensic Pedigree Analysis and Relatedness Inference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pedtools >= 2.2.0
BuildRequires:    R-CRAN-ribd >= 1.5.0
BuildRequires:    R-CRAN-pedprobr >= 0.8
BuildRequires:    R-CRAN-pedmut >= 0.6
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-pedtools >= 2.2.0
Requires:         R-CRAN-ribd >= 1.5.0
Requires:         R-CRAN-pedprobr >= 0.8
Requires:         R-CRAN-pedmut >= 0.6
Requires:         R-CRAN-glue 

%description
Forensic applications of pedigree analysis, including likelihood ratios
for relationship testing, general relatedness inference, marker
simulation, and power analysis. General computation of exclusion powers is
based on Egeland et al. (2014) <doi:10.1016/j.fsigen.2013.05.001>. Several
functions deal specifically with family reunion cases, implementing and
developing ideas from Kling et al. (2017)
<doi:10.1016/j.fsigen.2017.08.006>. A novelty of 'forrel' is the ability
to model background inbreeding in forensic pedigree computations.  This
can have significant impact in applications, as exemplified in Vigeland
and Egeland (2019) <doi:10.1016/j.fsigss.2019.10.175>. 'forrel' is part of
the ped suite, a collection of packages for pedigree analysis. In
particular, 'forrel' imports 'pedtools' for creating and manipulating
pedigrees and markers, 'pedprobr' for likelihood computations, and
'pedmut' for mutation modelling.  Pedigree data may be created from
scratch, or loaded from text files. Data import from the 'Familias'
software (Egeland et al. (2000) <doi:10.1016/S0379-0738(00)00147-X>) is
supported.

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
