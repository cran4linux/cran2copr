%global packname  bestNormalize
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Normalizing Transformation Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-LambertW >= 0.6.5
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-butcher 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-LambertW >= 0.6.5
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-tibble 
Requires:         R-methods 
Requires:         R-CRAN-butcher 
Requires:         R-CRAN-purrr 

%description
Estimate a suite of normalizing transformations, including a new
adaptation of a technique based on ranks which can guarantee normally
distributed transformed data if there are no ties: ordered quantile
normalization (ORQ). ORQ normalization combines a rank-mapping approach
with a shifted logit approximation that allows the transformation to work
on data outside the original domain. It is also able to handle new data
within the original domain via linear interpolation. The package is built
to estimate the best normalizing transformation for a vector consistently
and accurately. It implements the Box-Cox transformation, the Yeo-Johnson
transformation, three types of Lambert WxF transformations, and the
ordered quantile normalization transformation. It estimates the
normalization efficacy of other commonly used transformations, and it
allows users to specify custom transformations or normalization
statistics. Finally, functionality can be integrated into a machine
learning workflow via recipes.

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
