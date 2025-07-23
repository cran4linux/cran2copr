%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rCBA
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          CBA Classifier

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-TunePareto 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-TunePareto 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides implementations of a classifier based on the "Classification
Based on Associations" (CBA). It can be used for building classification
models from association rules. Rules are pruned in the order of precedence
given by the sort criteria and a default rule is added. The final
classifier labels provided instances. CBA was originally proposed by Liu,
B. Hsu, W. and Ma, Y. Integrating Classification and Association Rule
Mining. Proceedings KDD-98, New York, 27-31 August. AAAI. pp80-86 (1998,
ISBN:1-57735-070-7).

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
