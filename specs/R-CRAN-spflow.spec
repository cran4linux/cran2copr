%global __brp_check_rpaths %{nil}
%global packname  spflow
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Econometric Interaction Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-utils 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-Rdpack 
Requires:         R-utils 

%description
Efficient estimation of spatial econometric models of origin-destination
flows, which may exhibit spatial autocorrelation in the dependent
variable, the explanatory variables or both. The model is the one proposed
by LeSage and Pace (2008) <doi:10.1111/j.1467-9787.2008.00573.x>, who
develop a matrix formulation that exploits the relational structure of
flow data. The estimation procedures follow most closely those outlined by
Dargel (2021) (preprint available at
<https://www.tse-fr.eu/fr/publications/revisiting-estimation-methods-spatial-econometric-interaction-models>).

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
