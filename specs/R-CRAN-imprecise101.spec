%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  imprecise101
%global packver   0.2.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Introduction to Imprecise Probabilities

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tolerance 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-pscl 
Requires:         R-stats 
Requires:         R-CRAN-tolerance 
Requires:         R-graphics 
Requires:         R-CRAN-pscl 

%description
An imprecise inference presented in the study of Walley (1996)
<doi:10.1111/j.2517-6161.1996.tb02065.x> is one of the statistical
reasoning methods when prior information is unavailable. Functions and
utils needed for illustrating this inferential paradigm are implemented
for classroom teaching and further comprehensive research. Two imprecise
models are demonstrated using multinomial data and 2x2 contingency table
data. The concepts of prior ignorance and imprecision are discussed in
lower and upper probabilities. Representation invariance principle,
hypothesis testing, decision-making, and further generalization are also
illustrated.

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
