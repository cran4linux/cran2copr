%global __brp_check_rpaths %{nil}
%global packname  DA
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Discriminant Analysis for Evolutionary Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-adegenet 
BuildRequires:    R-CRAN-lfda 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-klaR 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rARPACK 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-adegenet 
Requires:         R-CRAN-lfda 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-klaR 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rARPACK 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Discriminant Analysis (DA) for evolutionary inference (Qin, X. et al,
2020, <doi:10.22541/au.159256808.83862168>), especially for population
genetic structure and community structure inference. This package
incorporates the commonly used linear and non-linear, local and global
supervised learning approaches (discriminant analysis), including Linear
Discriminant Analysis of Kernel Principal Components (LDAKPC), Local
(Fisher) Linear Discriminant Analysis (LFDA), Local (Fisher) Discriminant
Analysis of Kernel Principal Components (LFDAKPC) and Kernel Local
(Fisher) Discriminant Analysis (KLFDA). These discriminant analyses can be
used to do ecological and evolutionary inference, including demography
inference, species identification, and population/community structure
inference.

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
