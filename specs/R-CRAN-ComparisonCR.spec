%global packname  ComparisonCR
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          2%{?dist}
Summary:          Comparison of Cumulative Incidence Between Two Groups UnderCompeting Risks

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-CIFsmry 
BuildRequires:    R-CRAN-cmprsk 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-boot 
Requires:         R-CRAN-CIFsmry 
Requires:         R-CRAN-cmprsk 

%description
Statistical methods for competing risks data in comparing cumulative
incidence function curves between two groups, including overall hypothesis
tests and arbitrary tests in Lyu et al. (2020) <doi:10.1002/pst.2028>, and
the fixed-point tests in Chen et al. (2018)
<doi:10.1080/03610918.2018.1476697>.

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
