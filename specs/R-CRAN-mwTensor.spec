%global __brp_check_rpaths %{nil}
%global packname  mwTensor
%global packver   0.99.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.5
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Way Component Analysis

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-CRAN-nnTensor 
BuildRequires:    R-CRAN-ccTensor 
BuildRequires:    R-CRAN-ica 
BuildRequires:    R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rTensor 
Requires:         R-CRAN-nnTensor 
Requires:         R-CRAN-ccTensor 
Requires:         R-CRAN-ica 
Requires:         R-CRAN-igraph 

%description
For single tensor data, any matrix factorization method can be specified
the matricised tensor in each dimension by Multi-way Component Analysis
(MWCA). An originally extended MWCA is also implemented to specify and
decompose multiple matrices and tensors simultaneously (CoupledMWCA). See
the reference section of GitHub README.md
<https://github.com/rikenbit/mwTensor>, for details of the methods.

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
