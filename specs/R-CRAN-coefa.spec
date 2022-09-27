%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coefa
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Meta Analysis of Factor Analysis Based on CO-Occurrence Matrices

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-purrr 

%description
Provide a series of functions to conduct a meta analysis of factor
analysis based on co-occurrence matrices. The tool can be used to solve
the factor structure (i.e. inner structure of a construct, or scale)
debate in several disciplines, such as psychology, psychiatry, management,
education so on. References: Shafer (2005)
<doi:10.1037/1040-3590.17.3.324>; Shafer (2006) <doi:10.1002/jclp.20213>;
Loeber and Schmaling (1985) <doi:10.1007/BF00910652>.

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
