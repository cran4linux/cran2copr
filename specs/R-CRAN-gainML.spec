%global packname  gainML
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning-Based Analysis of Potential Power Gain from Passive Device Installation on Wind Turbine Generators

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fields >= 9.0
BuildRequires:    R-CRAN-FNN >= 1.1
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-fields >= 9.0
Requires:         R-CRAN-FNN >= 1.1
Requires:         R-utils 
Requires:         R-stats 

%description
Provides an effective machine learning-based tool that quantifies the gain
of passive device installation on wind turbine generators. H. Hwangbo, Y.
Ding, and D. Cabezon (2019) <arXiv:1906.05776>.

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
