%global packname  blocksdesign
%global packver   4.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.7
Release:          1%{?dist}%{?buildtag}
Summary:          Nested and Crossed Block Designs for Factorial and Unstructured Treatment Sets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-PolynomF 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-PolynomF 

%description
Constructs treatment and block designs for linear treatment models with
crossed or nested block factors. The treatment design can be any feasible
linear model and the block design can be any feasible combination of
crossed or nested block factors. The block design is a sum of one or more
block factors and the block design is optimized sequentially with the
levels of each successive block factor optimized conditional on all
previously optimized block factors. D-optimality is used throughout except
for square or rectangular lattice block designs which are constructed
algebraically using mutually orthogonal Latin squares. Crossed block
designs with interaction effects are optimized using a weighting scheme
which allows for differential weighting of first and second-order block
effects. Outputs include a table showing the allocation of treatments to
blocks and tables showing the achieved D-efficiency factors for each block
and treatment design. Edmondson, R.N. Multi-level Block Designs for
Comparative Experiments. JABES 25, 500–522 (2020).
<doi:10.1007/s13253-020-00416-0>.

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
