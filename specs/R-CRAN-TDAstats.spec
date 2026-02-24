%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TDAstats
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Pipeline for Topological Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-methods >= 3.6.2
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
Requires:         R-methods >= 3.6.2
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-Rcpp >= 0.12.15

%description
A comprehensive toolset for any useR conducting topological data analysis,
specifically via the calculation of persistent homology in a Vietoris-Rips
complex. The tools this package currently provides can be conveniently
split into three main sections: (1) calculating persistent homology; (2)
conducting statistical inference on persistent homology calculations; (3)
visualizing persistent homology and statistical inference. The published
form of TDAstats can be found in Wadhwa et al. (2018)
<doi:10.21105/joss.00860>. For a general background on computing
persistent homology for topological data analysis, see Otter et al. (2017)
<doi:10.1140/epjds/s13688-017-0109-5>. To learn more about how the
permutation test is used for nonparametric statistical inference in
topological data analysis, read Robinson & Turner (2017)
<doi:10.1007/s41468-017-0008-7>. To learn more about how TDAstats
calculates persistent homology, you can visit the GitHub repository for
Ripser, the software that works behind the scenes at
<https://github.com/Ripser/ripser>. This package has been published as
Wadhwa et al. (2018) <doi:10.21105/joss.00860>.

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
