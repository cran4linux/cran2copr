%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TAD
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Realize the Trait Abundance Distribution

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-mblm >= 0.12
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-mblm >= 0.12
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-stats 

%description
The “TAD” package compiled an analytical framework based on an analysis of
the shape of the trait abundance distributions to better understand
community assembly processes, and predict community dynamics under
environmental changes. This framework mobilized a study of the
relationship between the moments describing the shape of the
distributions: the skewness and the kurtosis (SKR). The SKR allows the
identification of commonalities in the shape of trait distributions across
contrasting communities. Derived from the SKR, we developed mathematical
parameters that summarise the complex pattern of distributions by
assessing (i) the R², (ii) the Y-intercept, (iii) the slope, (iv) the
functional stability of community (TADstab), and, (v) the distance from
specific distribution families (i.e., the distance from the skew-uniform
family a limit to the highest degree of evenness: TADeve).

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
