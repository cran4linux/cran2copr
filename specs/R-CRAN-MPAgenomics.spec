%global __brp_check_rpaths %{nil}
%global packname  MPAgenomics
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Patient Analysis of Genomic Markers

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-changepoint >= 1.1
BuildRequires:    R-CRAN-HDPenReg >= 0.90
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-spikeslab 
Requires:         R-CRAN-changepoint >= 1.1
Requires:         R-CRAN-HDPenReg >= 0.90
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-spikeslab 

%description
Preprocessing and analysis of genomic data. 'MPAgenomics' provides
wrappers from commonly used packages to streamline their repeated
manipulation, offering an easy-to-use pipeline. The segmentation of
successive multiple profiles is performed with an automatic choice of
parameters involved in the wrapped packages. Considering multiple profiles
in the same time, 'MPAgenomics' wraps efficient penalized regression
methods to select relevant markers associated with a given outcome.
Grimonprez et al. (2014) <doi:10.1186/s12859-014-0394-y>.

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
