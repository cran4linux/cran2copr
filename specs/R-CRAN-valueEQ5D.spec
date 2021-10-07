%global __brp_check_rpaths %{nil}
%global packname  valueEQ5D
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Scoring EQ-5d Descriptive System

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-utils 
Requires:         R-CRAN-testthat 
Requires:         R-utils 

%description
EQ-5D is a standard instrument (<https://euroqol.org/eq-5d-instruments/>)
that measures the quality of life often used in clinical and economic
evaluations of health care technologies. Both adult versions of EQ-5D
(EQ-5D-3L and EQ-5D-5L) contain a descriptive system and visual analog
scale. The descriptive system measures the patient's health in 5
dimensions: the 5L versions has 5 levels and 3L version has 3 levels. The
descriptive system scores are usually converted to index values using
country specific values sets (that incorporates the country preferences).
This package allows the calculation of both descriptive system scores to
the index value scores. The value sets for EQ-5D-3L are from the
references mentioned in the website
<https://euroqol.org/eq-5d-instruments/eq-5d-3l-about/valuation/> The
value sets for EQ-5D-3L for a total of 31 countries are used for the
valuation (see the user guide for a complete list of references). The
value sets for EQ-5D-5L are obtained from references mentioned in the
<https://euroqol.org/eq-5d-instruments/eq-5d-5l-about/valuation-standard-value-sets/>
and other sources. The value sets for EQ-5D-5L for a total of 17 countries
are used for the valuation (see the user guide for a complete list of
references). The package can also be used to map 5L scores to 3L index
values for 10 countries: Denmark, France, Germany, Japan, Netherlands,
Spain, Thailand, UK, USA, and Zimbabwe. The value set and method for
mapping are obtained from Van Hout et al (2012) <doi:
10.1016/j.jval.2012.02.008>.

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
