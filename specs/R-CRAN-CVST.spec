%global __brp_check_rpaths %{nil}
%global packname  CVST
%global packver   0.2-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Cross-Validation via Sequential Testing

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-Matrix 

%description
The fast cross-validation via sequential testing (CVST) procedure is an
improved cross-validation procedure which uses non-parametric testing
coupled with sequential analysis to determine the best parameter set on
linearly increasing subsets of the data. By eliminating under-performing
candidates quickly and keeping promising candidates as long as possible,
the method speeds up the computation while preserving the capability of a
full cross-validation. Additionally to the CVST the package contains an
implementation of the ordinary k-fold cross-validation with a flexible and
powerful set of helper objects and methods to handle the overall model
selection process. The implementations of the Cochran's Q test with
permutations and the sequential testing framework of Wald are generic and
can therefore also be used in other contexts.

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
