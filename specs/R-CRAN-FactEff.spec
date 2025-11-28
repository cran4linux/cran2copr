%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FactEff
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Efficiencies of Block Designs for Factorial and Fractional Factorial Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-htmltools 

%description
Opens a 'shiny' app which supports theoretical and computational analysis
of block designs for symmetrical and mixed level factorial experiments.
This package includes tools to check whether a design has orthogonal
factorial structure (OFS) with balance or not and is able to find the
orthogonality deviation value if not having OFS. This package includes
function to evaluate efficiency factor of all factorial effects in two
situations, in the first situation if the design is verified with OFS and
balance then calculate the efficiencies of all factorial effects using a
specific analytical procedure and in the second situation if the design is
verified with non-OFS and balance then a new general method has been
developed and used to calculate efficiencies under the condition that the
design should be proper and equi-replicated, See Gupta, S.C. and Mukerjee,
R. (1987): "A Calculus for factorial arrangements".  Lecture Notes in
Statistics. No. 59, Springer-Verlag, Berlin, New York,
<doi:10.1007/978-1-4419-8730-3>. For the easy use of package, 'shiny' app
is used for giving inputs and inputs validation.

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
