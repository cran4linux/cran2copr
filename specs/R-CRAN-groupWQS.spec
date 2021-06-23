%global __brp_check_rpaths %{nil}
%global packname  groupWQS
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          2%{?dist}%{?buildtag}
Summary:          Grouped Weighted Quantile Sum Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-glm2 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-rjags 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-glm2 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-CRAN-rjags 

%description
Fits weighted quantile sum (WQS) regressions for one or more chemical
groups with continuous or binary outcomes. Wheeler D, Czarnota J.(2016)
<doi:10.1289/isee.2016.4698>.

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
