%global packname  ciuupi2
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Kabaila and Giri (2009) Confidence Interval

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-functional 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-PreciseSums 
BuildRequires:    R-CRAN-statmod 
Requires:         R-CRAN-functional 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-PreciseSums 
Requires:         R-CRAN-statmod 

%description
Computes a confidence interval for a specified linear combination of the
regression parameters in a linear regression model with iid normal errors
with unknown variance when there is uncertain prior information that a
distinct specified linear combination of the regression parameters takes a
specified number. This confidence interval, found by numerical nonlinear
constrained optimization, has the required minimum coverage and utilizes
this uncertain prior information through desirable expected length
properties. This confidence interval is proposed by Kabaila, P. and Giri,
K. (2009) <doi:10.1016/j.jspi.2009.03.018>.

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
