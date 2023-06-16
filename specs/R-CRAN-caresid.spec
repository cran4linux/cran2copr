%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  caresid
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Correspondence Analysis Plot and Associations Visualisation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-graphics >= 4.2.0
BuildRequires:    R-stats >= 4.2.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-ggrepel >= 0.9.0
BuildRequires:    R-CRAN-ca >= 0.71
Requires:         R-graphics >= 4.2.0
Requires:         R-stats >= 4.2.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-ggrepel >= 0.9.0
Requires:         R-CRAN-ca >= 0.71

%description
Performs a Correspondence Analysis (CA) on a contingency table and creates
a scatterplot of the row and column points on the selected dimensions.
Optionally, the function can add segments to the plot to visualize
significant associations between row and column categories on the basis of
positive (unadjusted) standardized residuals larger than a given
threshold.

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
