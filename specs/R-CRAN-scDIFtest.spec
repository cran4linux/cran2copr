%global packname  scDIFtest
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Item-Wise Score-Based DIF Detection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-mirt 
Requires:         R-CRAN-zoo 

%description
Detection of item-wise Differential Item Functioning (DIF) in fitted
'mirt', 'multipleGroup' or 'bfactor' models using score-based structural
change tests. Under the hood the sctest() function from the 'strucchange'
package is used.

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
