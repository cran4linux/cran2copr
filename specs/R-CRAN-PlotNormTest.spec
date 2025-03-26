%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PlotNormTest
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical Univariate/Multivariate Assessments for Normality Assumption

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MatrixExtra 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MatrixExtra 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rlang 

%description
Graphical methods testing multivariate normality assumption. Methods
including assessing score function, and moment generating
functions,independent transformations and linear transformations. For more
details see Tran (2024),"Contributions to Multivariate Data Science:
Assessment and Identification of Multivariate Distributions and Supervised
Learning for Groups of Objects." , PhD thesis,
<https://our.oakland.edu/items/c8942577-2562-4d2f-8677-cb8ec0bf6234>.

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
