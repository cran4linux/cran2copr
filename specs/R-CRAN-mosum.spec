%global __brp_check_rpaths %{nil}
%global packname  mosum
%global packver   1.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Moving Sum Based Procedures for Changes in the Mean

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-plot3D 
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-plot3D 

%description
Implementations of MOSUM-based statistical procedures and algorithms for
detecting multiple changes in the mean. This comprises the MOSUM procedure
for estimating multiple mean changes from Eichinger and Kirch (2018)
<doi:10.3150/16-BEJ887> and the multiscale algorithmic extension from Cho
and Kirch (2021) <arXiv:1910.12486>, as well as the bootstrap procedure
for generating confidence intervals about the locations of change points
as proposed in Cho and Kirch (2021) <arXiv:2106.12844>. See also Meier,
Kirch and Cho (2021) <doi:10.18637/jss.v097.i08> which accompanies the R
package.

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
