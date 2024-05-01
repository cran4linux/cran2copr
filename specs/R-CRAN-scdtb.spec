%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scdtb
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Single Case Design Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-broom.mixed 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mmcards 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
Requires:         R-CRAN-broom.mixed 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mmcards 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 

%description
In some situations where researchers would like to demonstrate causal
effects, it is hard to obtain a sample size that would allow for a
well-powered randomized controlled trial. Single case designs are
experimental designs that can be used to demonstrate causal effects with
only one participant or with only a few participants. The 'scdtb' package
provides a suite of tools for analyzing data from studies that use single
case designs. The nap() function can be used to compute the nonoverlap of
all pairs as outlined by the What Works Clearinghouse (2022)
<https://ies.ed.gov/ncee/wwc/Handbooks>. The package also offers the
mixed_model_analysis() and cross_lagged() functions which implement mixed
effects models and cross lagged analyses as described in Maric & van der
Werff (2020) <doi:10.4324/9780429273872-9>. The randomization_test()
function implements randomization tests based on methods presented in
Onghena (2020) <doi:10.4324/9780429273872-8>. The scdtb() 'shiny'
application can be used to upload single case design data and access
various 'scdtb' tools for plotting and analysis.

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
