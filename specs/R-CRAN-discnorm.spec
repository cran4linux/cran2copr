%global packname  discnorm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Test for Discretized Normality in Ordinal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-sirt 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-psych 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-sirt 
Requires:         R-MASS 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-psych 

%description
Tests whether multivariate ordinal data may stem from discretizing a
multivariate normal distribution. The test is described by Foldnes and
Grønneberg (2019) <doi:10.1080/10705511.2019.1673168>.

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
