%global __brp_check_rpaths %{nil}
%global packname  Dire
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Regressions with a Latent Outcome Variable

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-Rcpp 

%description
Fit linear models, estimating score distributions for groups of people,
following Cohen and Jiang (1999) <doi:10.2307/2669917>. In this model, the
response is a latent trait (such as student ability) and raw item
responses are combined with item difficulties in an item response theory
(IRT) framework to form a density for each unit (student). This latent
trait is then integrated out. This software is intended to fit the same
models as the existing software 'AM' <http://am.air.org/>.

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
