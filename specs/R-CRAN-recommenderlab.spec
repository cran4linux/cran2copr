%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  recommenderlab
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Lab for Developing and Testing Recommender Algorithms

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-proxy >= 0.4.26
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-registry 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-recosystem 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-proxy >= 0.4.26
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-registry 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-recosystem 
Requires:         R-CRAN-matrixStats 

%description
Provides a research infrastructure to develop and evaluate collaborative
filtering recommender algorithms. This includes a sparse representation
for user-item matrices, many popular algorithms, top-N recommendations,
and cross-validation. Hahsler (2022) <doi:10.48550/arXiv.2205.12371>.

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
