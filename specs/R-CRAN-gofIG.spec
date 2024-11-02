%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gofIG
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit Tests for the Inverse Gaussian Distribution

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rmutil 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rmutil 

%description
We implement various tests for the composite hypothesis of testing the fit
to the family of inverse Gaussian distributions. Included are methods
presented by Allison, J.S., Betsch, S., Ebner, B., and Visagie, I.J.H.
(2022) <doi:10.48550/arXiv.1910.14119>, as well as two tests from Henze
and Klar (2002) <doi:10.1023/A:1022442506681>. Additionally, the package
implements a test proposed by Baringhaus and Gaigall (2015)
<doi:10.1016/j.jmva.2015.05.013>. For each test a parametric bootstrap
procedure is implemented.

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
