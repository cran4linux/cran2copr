%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MRZero
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Diet Mendelian Randomization

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg >= 5.01
BuildRequires:    R-CRAN-plotly >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 1.0.1
BuildRequires:    R-CRAN-robustbase >= 0.92.6
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-quantreg >= 5.01
Requires:         R-CRAN-plotly >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 1.0.1
Requires:         R-CRAN-robustbase >= 0.92.6
Requires:         R-methods 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-glmnet 

%description
Encodes several methods for performing Mendelian randomization analyses
with summarized data. Similar to the 'MendelianRandomization' package, but
with fewer bells and whistles, and less frequent updates. As described in
Yavorska (2017) <doi:10.1093/ije/dyx034> and Broadbent (2020)
<doi:10.12688/wellcomeopenres.16374.2>.

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
