%global packname  chngpt
%global packver   2020.8-29
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2020.8.29
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Hypothesis Testing for Threshold Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-survival 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-kyotil 
BuildRequires:    R-boot 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lme4 
Requires:         R-survival 
Requires:         R-splines 
Requires:         R-CRAN-kyotil 
Requires:         R-boot 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-lme4 

%description
Threshold regression models are also called two-phase regression,
broken-stick regression, split-point regression, structural change models,
and regression kink models, with and without interaction terms. Methods
for both continuous and discontinuous threshold models are included, but
the support for the former is much greater. This package is described in
Fong, Huang, Gilbert and Permar (2017) <DOI:10.1186/s12859-017-1863-x>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
