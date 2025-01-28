%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Reacnorm
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Perform a Partition of Variance of Reaction Norms

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cubature >= 1.4
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-cubature >= 1.4
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-matrixStats 

%description
Partitions the phenotypic variance of a plastic trait, studied through its
reaction norm. The variance partition distinguishes between the variance
arising from the average shape of the reaction norms (V_Plas) and the
(additive) genetic variance . The latter is itself separated into an
environment-blind component (V_G/V_A) and the component arising from
plasticity (V_GxE/V_AxE). The package also provides a way to further
partition V_Plas into aspects (slope/curvature) of the shape of the
average reaction norm (pi-decomposition) and partition V_Add
(gamma-decomposition) and V_AxE (iota-decomposition) into the impact of
genetic variation in the reaction norm parameters. Reference: de
Villemereuil & Chevin (2025) <doi:10.32942/X2NC8B>.

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
