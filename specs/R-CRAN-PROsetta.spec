%global __brp_check_rpaths %{nil}
%global packname  PROsetta
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Linking Patient-Reported Outcomes Measures

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-equate 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-CRAN-plink 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvnfast 
Requires:         R-CRAN-equate 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-mirt 
Requires:         R-CRAN-plink 
Requires:         R-CRAN-psych 
Requires:         R-methods 
Requires:         R-CRAN-mvnfast 

%description
Perform scale linking to establish relationships between instruments that
measure similar constructs according to the PROsetta Stone methodology, as
in Choi, Schalet, Cook, & Cella (2014) <doi:10.1037/a0035768>.

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
