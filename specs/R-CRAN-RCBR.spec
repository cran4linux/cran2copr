%global packname  RCBR
%global packver   0.5.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.9
Release:          1%{?dist}%{?buildtag}
Summary:          Random Coefficient Binary Response Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rmosek 
BuildRequires:    R-CRAN-REBayes 
BuildRequires:    R-CRAN-orthopolynom 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-Rmosek 
Requires:         R-CRAN-REBayes 
Requires:         R-CRAN-orthopolynom 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-mvtnorm 

%description
Nonparametric maximum likelihood estimation methods for random coefficient
binary response models and some related functionality for sequential
processing of hyperplane arrangements. See J. Gu and R. Koenker (2020)
<DOI:10.1080/01621459.2020.1802284>.

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
