%global packname  pathmodelfit
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Path Component Fit Indices for Latent Structural Equation Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
Requires:         R-CRAN-lavaan 

%description
Functions for computing fit indices for evaluating the path component of
latent variable structural equation models. Available fit indices include
RMSEA-P and NSCI-P originally presented and evaluated by Williams and
O'Boyle (2011) <doi:10.1177/1094428110391472> and demonstrated by O'Boyle
and Williams (2011) <doi:10.1037/a0020539> and Williams, O'Boyle, & Yu
(2020) <doi:10.1177/1094428117736137>. Also included are fit indices
described by Hancock and Mueller (2011) <doi:10.1177/0013164410384856>.

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
