%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Anthropometry
%global packver   1.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.21
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for Anthropometric Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-shapes 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-archetypes 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-ddalpha 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-ICGE 
BuildRequires:    R-CRAN-cluster 
Requires:         R-CRAN-shapes 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-archetypes 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-ddalpha 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-ICGE 
Requires:         R-CRAN-cluster 

%description
Statistical methodologies especially developed to analyze anthropometric
data. These methods are aimed at providing effective solutions to some
commons problems related to Ergonomics and Anthropometry. They are based
on clustering, the statistical concept of data depth, statistical shape
analysis and archetypal analysis. Please see Vinue (2017)
<doi:10.18637/jss.v077.i06>.

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
