%global packname  ebmstate
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Empirical Bayes Multi-State Cox Model

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-survival >= 2.44.1.1
BuildRequires:    R-CRAN-mstate >= 0.2.11
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-HDInterval 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-survival >= 2.44.1.1
Requires:         R-CRAN-mstate >= 0.2.11
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-HDInterval 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
Implements an empirical Bayes, multi-state Cox model for survival
analysis. Run "?'ebmstate-package'" for details. See also Schall (1991)
<doi:10.1093/biomet/78.4.719>.

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
