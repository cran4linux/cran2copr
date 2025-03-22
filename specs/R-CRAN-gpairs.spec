%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gpairs
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Generalized Pairs Plot

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-barcode 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-methods 
Requires:         R-grid 
Requires:         R-CRAN-barcode 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-vcd 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-colorspace 
Requires:         R-methods 

%description
Offers a generalization of the scatterplot matrix based on the recognition
that most datasets include both categorical and quantitative information.
Traditional grids of scatterplots often obscure important features of the
data when one or more variables are categorical but coded as numerical.
The generalized pairs plot offers a range of displays of paired
combinations of categorical and quantitative variables. Emerson et al.
(2013) <DOI:10.1080/10618600.2012.694762>.

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
