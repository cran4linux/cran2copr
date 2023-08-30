%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  exactamente
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Explore the Exact Bootstrap Method

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 

%description
Researchers often use the bootstrap to understand a sample drawn from a
population with unknown distribution. The exact bootstrap method is a
practical tool for exploring the distribution of small sample size data.
For a sample of size n, the exact bootstrap method generates the entire
space of n to the power of n resamples and calculates all realizations of
the selected statistic. The 'exactamente' package includes functions for
implementing two bootstrap methods, the exact bootstrap and the regular
bootstrap. The exact_bootstrap() function applies the exact bootstrap
method following methodologies outlined in Kisielinska (2013)
<doi:10.1007/s00180-012-0350-0>. The regular_bootstrap() function offers a
more traditional bootstrap approach, where users can determine the number
of resamples. The e_vs_r() function allows users to directly compare
results from these bootstrap methods. To augment user experience,
'exactamente' includes the function exactamente_app() which launches an
interactive 'shiny' web application. This application facilitates
exploration and comparison of the bootstrap methods, providing options for
modifying various parameters and visualizing results.

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
