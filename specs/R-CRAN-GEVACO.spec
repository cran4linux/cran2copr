%global packname  GEVACO
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Joint Test of Gene and GxE Interactions via Varying Coefficients

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-RLRsim 
BuildRequires:    R-stats 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-RLRsim 
Requires:         R-stats 

%description
A novel statistical model to detect the joint genetic and dynamic
gene-environment (GxE) interaction with continuous traits in genetic
association studies. It uses varying-coefficient models to account for
different GxE trajectories, regardless whether the relationship is linear
or not. The package includes one function, GxEtest(), to test a single
genetic variant (e.g., a single nucleotide polymorphism or SNP), and
another function, GxEscreen(), to test for a set of genetic variants. The
method involves a likelihood ratio test described in Crainiceanu, C. M.,
and Ruppert, D. (2004) <doi:10.1111/j.1467-9868.2004.00438.x>.

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
