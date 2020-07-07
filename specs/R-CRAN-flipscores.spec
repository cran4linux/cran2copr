%global packname  flipscores
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          Robust Score Testing in GLMs, by Sign-Flip Contributions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-flip 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-methods 
Requires:         R-CRAN-flip 
Requires:         R-CRAN-car 
Requires:         R-MASS 
Requires:         R-CRAN-plyr 
Requires:         R-methods 

%description
Provides robust tests for testing in GLMs, by sign-flipping score
contributions. The tests are robust against overdispersion,
heteroscedasticity and, in some cases, ignored nuisance variables. See
Hemerik, Goeman and Finos (2020) <doi:10.1111/rssb.12369>.

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
