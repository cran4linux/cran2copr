%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PBIBD
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Partially Balanced Incomplete Block Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The PBIB designs are important type of incomplete block designs having
wide area of their applications for example in agricultural experiments,
in plant breeding, in sample surveys etc. This package constructs various
series of PBIB designs and assists in checking all the necessary
conditions of PBIB designs and the association scheme on which these
designs are based on. It also assists in calculating the efficiencies of
PBIB designs with any number of associate classes. The package also
constructs Youden-m square designs which are Row-Column designs for the
two-way elimination of heterogeneity. The incomplete columns of these
Youden-m square designs constitute PBIB designs. With the present
functionality, the package will be of immense importance for the
researchers as it will help them to construct PBIB designs, to check if
their PBIB designs and association scheme satisfy various necessary
conditions for the existence, to calculate the efficiencies of PBIB
designs based on any association scheme and to construct Youden-m square
designs for the two-way elimination of heterogeneity. R. C. Bose and K. R.
Nair (1939) <http://www.jstor.org/stable/40383923>.

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
