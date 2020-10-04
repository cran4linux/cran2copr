%global packname  CorrMixed
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Estimate Correlations Between Repeatedly Measured Endpoints(E.g., Reliability) Based on Linear Mixed-Effects Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-psych 
Requires:         R-nlme 
Requires:         R-CRAN-psych 

%description
In clinical practice and research settings in medicine and the behavioral
sciences, it is often of interest to quantify the correlation of a
continuous endpoint that was repeatedly measured (e.g., test-retest
correlations, ICC, etc.). This package allows for estimating these
correlations based on mixed-effects models. Part of this software has been
developed using funding provided from the European Union's 7th Framework
Programme for research, technological development and demonstration under
Grant Agreement no 602552.

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

%files
%{rlibdir}/%{packname}
