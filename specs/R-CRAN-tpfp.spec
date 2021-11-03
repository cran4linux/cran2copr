%global __brp_check_rpaths %{nil}
%global packname  tpfp
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Counts the Number of True Positives and False Positives

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-tcltk 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-readxl 
Requires:         R-tcltk 

%description
Calculates the number of true positives and false positives from a dataset
formatted for Jackknife alternative free-response receiver operating
characteristic which is used for statistical analysis which is explained
in the book 'Chakraborty' 'DP' (2017), "Observer Performance Methods for
Diagnostic Imaging - Foundations, Modeling, and Applications with R-Based
Examples", Taylor-Francis <https://www.crcpress.com/9781482214840>.

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
