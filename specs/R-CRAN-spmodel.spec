%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spmodel
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Statistical Modeling and Prediction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-parallel 
Requires:         R-graphics 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-parallel 

%description
Fit, summarize, and predict for a variety of spatial statistical models
applied to point-referenced and areal (lattice) data. Parameters are
estimated using various methods. Additional modeling features include
anisotropy, non-spatial random effects, partition factors, big data
approaches, and more. Model-fit statistics are used to summarize,
visualize, and compare models. Predictions at unobserved locations are
readily obtainable. For additional details, see Dumelle et al. (2023)
<doi:10.1371/journal.pone.0282524>.

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
