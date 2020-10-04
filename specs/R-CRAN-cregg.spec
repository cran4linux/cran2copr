%global packname  cregg
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          2%{?dist}%{?buildtag}
Summary:          Simple Conjoint Tidying, Analysis, and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survey >= 3.33
BuildRequires:    R-CRAN-sandwich >= 2.4.0
BuildRequires:    R-CRAN-ggplot2 >= 2.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-ggstance 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
Requires:         R-CRAN-survey >= 3.33
Requires:         R-CRAN-sandwich >= 2.4.0
Requires:         R-CRAN-ggplot2 >= 2.0
Requires:         R-stats 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-ggstance 
Requires:         R-CRAN-scales 
Requires:         R-utils 

%description
Simple tidying, analysis, and visualization of conjoint (factorial)
experiments, including estimation and visualization of average marginal
component effects ('AMCEs') and marginal means ('MMs') for weighted and
un-weighted survey data, along with useful reference category diagnostics
and statistical tests. Estimation of 'AMCEs' is based upon methods
described by Hainmueller, Hopkins, and Yamamoto (2014)
<doi:10.1093/pan/mpt024>.

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
