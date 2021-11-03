%global __brp_check_rpaths %{nil}
%global packname  crrcbcv
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bias-Corrected Variance for Competing Risks Regression with Clustered Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-crrSC 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
Requires:         R-CRAN-crrSC 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-survival 
Requires:         R-stats 

%description
A user friendly function 'crrcbcv' to compute bias-corrected variances for
competing risks regression models using proportional subdistribution
hazards with small-sample clustered data. Four types of bias correction
are included: the MD-type bias correction by Mancl and DeRouen (2001)
<doi:10.1111/j.0006-341X.2001.00126.x>, the KC-type bias correction by
Kauermann and Carroll (2001) <doi:10.1198/016214501753382309>, the FG-type
bias correction by Fay and Graubard (2001)
<doi:10.1111/j.0006-341X.2001.01198.x>, and the MBN-type bias correction
by Morel, Bokossa, and Neerchal (2003) <doi:10.1002/bimj.200390021>.

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
