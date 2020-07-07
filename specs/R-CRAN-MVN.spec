%global packname  MVN
%global packver   5.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.8
Release:          2%{?dist}
Summary:          Multivariate Normality Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-mvoutlier 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-car 
Requires:         R-methods 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-moments 
Requires:         R-MASS 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-mvoutlier 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-psych 
Requires:         R-boot 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-car 

%description
Performs multivariate normality tests and graphical approaches and
implements multivariate outlier detection and univariate normality of
marginal distributions through plots and tests, and performs multivariate
Box-Cox transformation (Korkmaz et al, (2014),
<https://journal.r-project.org/archive/2014-2/korkmaz-goksuluk-zararsiz.pdf>).

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
