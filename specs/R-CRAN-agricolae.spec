%global packname  agricolae
%global packver   1.3-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Procedures for Agricultural Research

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-klaR 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-AlgDesign 
BuildRequires:    R-graphics 
Requires:         R-CRAN-klaR 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-AlgDesign 
Requires:         R-graphics 

%description
Original idea was presented in the thesis "A statistical analysis tool for
agricultural research" to obtain the degree of Master on science, National
Engineering University (UNI), Lima-Peru. Some experimental data for the
examples come from the CIP and others research. Agricolae offers extensive
functionality on experimental design especially for agricultural and plant
breeding experiments, which can also be useful for other purposes. It
supports planning of lattice, Alpha, Cyclic, Complete Block, Latin Square,
Graeco-Latin Squares, augmented block, factorial, split and strip plot
designs. There are also various analysis facilities for experimental data,
e.g. treatment comparison procedures and several non-parametric tests
comparison, biodiversity indexes and consensus cluster.

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
