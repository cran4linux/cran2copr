%global packname  MolgenisArmadillo
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Armadillo Client for the Armadillo Service

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-aws.iam 
BuildRequires:    R-CRAN-aws.s3 
BuildRequires:    R-CRAN-MolgenisAuth 
BuildRequires:    R-CRAN-arrow 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-urltools 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-aws.iam 
Requires:         R-CRAN-aws.s3 
Requires:         R-CRAN-MolgenisAuth 
Requires:         R-CRAN-arrow 

%description
A set of functions to be able to manage data shared on a 'MOLGENIS
Armadillo' storage server ('MinIO').

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
