%global __brp_check_rpaths %{nil}
%global packname  tcplfit2
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Concentration-Response Modeling of HTS or Transcriptomics Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-future 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-stringr 

%description
Performs the basic concentration response curve fitting used in the 'tcpl'
package. It is a substitute for the original tcplFit() function (and
sub-functions) and allows a wider variety of concentration-response
models. All of the models included in the 'BMDExpress' package are now
part of this package, and the output includes a calculation of the bmd
(Benchmark Dose or concentration) value.

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
