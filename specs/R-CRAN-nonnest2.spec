%global __brp_check_rpaths %{nil}
%global packname  nonnest2
%global packver   0.5-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.5
Release:          2%{?dist}%{?buildtag}
Summary:          Tests of Non-Nested Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.6.6
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-lavaan >= 0.6.6
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-sandwich 

%description
Testing non-nested models via theory supplied by Vuong (1989)
<DOI:10.2307/1912557>. Includes tests of model distinguishability and of
model fit that can be applied to both nested and non-nested models. Also
includes functionality to obtain confidence intervals associated with AIC
and BIC. This material is partially based on work supported by the
National Science Foundation under Grant Number SES-1061334.

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
