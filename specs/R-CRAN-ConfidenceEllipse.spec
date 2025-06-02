%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ConfidenceEllipse
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of 2D and 3D Elliptical Joint Confidence Regions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-cellWise 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-cellWise 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 

%description
Computing elliptical joint confidence regions at a specified confidence
level. It provides the flexibility to estimate either classical or robust
confidence regions, which can be visualized in 2D or 3D plots. The
classical approach assumes normality and uses the mean and covariance
matrix to define the confidence regions. Alternatively, the robustified
version employs estimators like minimum covariance determinant (MCD) and
M-estimator, making them less sensitive to outliers and departures from
normality. Furthermore, the functions allow users to group the dataset
based on categorical variables and estimate separate confidence regions
for each group. This capability is particularly useful for exploring
potential differences or similarities across subgroups within a dataset.
Varmuza and Filzmoser (2009, ISBN:978-1-4200-5947-2). Johnson and Wichern
(2007, ISBN:0-13-187715-1). Raymaekers and Rousseeuw (2019)
<DOI:10.1080/00401706.2019.1677270>.

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
