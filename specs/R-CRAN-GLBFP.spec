%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GLBFP
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          General Linear Blend Frequency Polygon Density Estimation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 

%description
Implements nonparametric density estimation with Averaged Shifted
Histogram (ASH), Linear Blend Frequency Polygon (LBFP), and General Linear
Blend Frequency Polygon (GLBFP) estimators. The package provides pointwise
and grid-based estimation workflows, sparse-prefix grid-count computation,
plotting helpers, and plug-in bandwidth selection. Methodological
background follows Scott (1992) <doi:10.1002/9780470316849>, Terrell and
Scott (1985) <doi:10.1080/01621459.1985.10477163>, and Carbon and Duchesne
(2024) <doi:10.1007/s10463-023-00883-5>.

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
