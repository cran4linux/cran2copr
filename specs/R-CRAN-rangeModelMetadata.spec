%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rangeModelMetadata
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Provides Templates for Metadata Files Associated with Species Range Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-spocc 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BIEN 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-spocc 
Requires:         R-utils 
Requires:         R-CRAN-BIEN 
Requires:         R-CRAN-terra 

%description
Range Modeling Metadata Standards (RMMS) address three challenges: they
(i) are designed for convenience to encourage use, (ii) accommodate a wide
variety of applications, and (iii) are extensible to allow the community
of range modelers to steer it as needed. RMMS are based on a data
dictionary that specifies a hierarchical structure to catalog different
aspects of the range modeling process. The dictionary balances a
constrained, minimalist vocabulary to improve standardization with
flexibility for users to provide their own values. Merow et al. (2019)
<DOI:10.1111/geb.12993> describe the standards in more detail. Note that
users who prefer to use the R package 'ecospat' can obtain it from
<https://github.com/ecospat/ecospat>.

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
