%global packname  qtlcharts
%global packver   0.12-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.10
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Graphics for QTL Experiments

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-CRAN-qtl >= 1.30.4
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-qtl >= 1.30.4
Requires:         R-CRAN-htmlwidgets 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Web-based interactive charts (using D3.js) for the analysis of
experimental crosses to identify genetic loci (quantitative trait loci,
QTL) contributing to variation in quantitative traits. Broman (2015)
<doi:10.1534/genetics.114.172742>.

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
