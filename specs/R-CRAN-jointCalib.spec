%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jointCalib
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Joint Calibration of Totals and Quantiles

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-laeken 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ebal 
Requires:         R-CRAN-laeken 
Requires:         R-CRAN-sampling 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ebal 

%description
A small package containing functions to perform a joint calibration of
totals and quantiles. The calibration for totals is based on Deville and
Särndal (1992) <doi:10.1080/01621459.1992.10475217>, the calibration for
quantiles is based on Harms and Duchesne (2006)
<https://www150.statcan.gc.ca/n1/en/catalogue/12-001-X20060019255>. The
package uses standard calibration via the 'survey', 'sampling' or 'laeken'
packages. In addition, entropy balancing via the 'ebal' package and
empirical likelihood based on codes from Wu (2005)
<https://www150.statcan.gc.ca/n1/pub/12-001-x/2005002/article/9051-eng.pdf>
can be used. See the paper by Beręsewicz and Szymkowiak (2023) for details
<arXiv:2308.13281>.

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
